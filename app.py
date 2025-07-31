from flask import Flask, render_template, request, jsonify, redirect, url_for, flash


from models.job_application import JobApplication
from models.job_role import JobRole
from utils.storage_handler import save_jobs_to_file, load_jobs_from_file

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Load jobs on startup
job_list = load_jobs_from_file()

@app.route('/')
def dashboard():
    """Main dashboard showing overview and statistics"""
    if not job_list:
        stats = {}
        recent_jobs = []
    else:
        # Calculate statistics
        stats = {}
        for job in job_list:
            status = job.status
            stats[status] = stats.get(status, 0) + 1
        
        # Get recent jobs (last 5)
        recent_jobs = job_list[-5:] if len(job_list) >= 5 else job_list
        recent_jobs.reverse()  # Show most recent first
    
    return render_template('dashboard.html', stats=stats, recent_jobs=recent_jobs, total_jobs=len(job_list))

@app.route('/jobs')
def view_jobs():
    """View all job applications"""
    return render_template('jobs.html', jobs=job_list)

@app.route('/jobs/add', methods=['GET', 'POST'])
def add_job():
    """Add a new job application"""
    if request.method == 'POST':
        try:
            # Get form data
            company = request.form['company']
            date_applied = request.form['date_applied']
            domain = request.form['domain']
            position = request.form['position']
            experience = request.form['experience']
            tech_needed = request.form['tech_needed']
            resume_version = request.form['resume_version']
            notes = request.form['notes']
            
            # Create job role and application
            role = JobRole(domain, position, experience, tech_needed)
            job = JobApplication(company, date_applied, role, resume_version, notes)
            
            # Add to list and save
            job_list.append(job)
            save_jobs_to_file(job_list)
            
            flash(f'Job application for {company} added successfully!', 'success')
            return redirect(url_for('view_jobs'))
            
        except Exception as e:
            flash(f'Error adding job application: {str(e)}', 'error')
    
    return render_template('add_job.html')

@app.route('/jobs/<int:job_id>')
def job_detail(job_id):
    """View detailed information about a specific job"""
    if 0 <= job_id < len(job_list):
        job = job_list[job_id]
        return render_template('job_detail.html', job=job, job_id=job_id)
    else:
        flash('Job not found!', 'error')
        return redirect(url_for('view_jobs'))

@app.route('/jobs/<int:job_id>/update_status', methods=['POST'])
def update_job_status(job_id):
    """Update the status of a job application"""
    if 0 <= job_id < len(job_list):
        try:
            job = job_list[job_id]
            new_status = request.form['status']
            notes = request.form.get('notes', '')
            interview_scheduled = request.form.get('interview_scheduled') or None
            rounds_cleared = request.form.get('rounds_cleared', '').split(',')
            rounds_cleared = [round.strip() for round in rounds_cleared if round.strip()]

            status_change = {
                new_status: {
                    'notes': notes,
                    'interview_scheduled': interview_scheduled,
                    'rounds_cleared': rounds_cleared
                }
            }
            
            job.update_status(status_change)
            save_jobs_to_file(job_list)

            flash(f'Status updated to {new_status} successfully!', 'success')

            # Redirect based on referrer
            referrer = request.referrer
            if referrer and 'update-status' in referrer:
                return redirect(url_for('update_status_page'))
            elif referrer and 'search' in referrer:
                return redirect(url_for('search_jobs'))
            elif referrer and request.endpoint == 'dashboard':
                return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('job_detail', job_id=job_id))

        except Exception as e:
            flash(f'Error updating status: {str(e)}', 'error')
    else:
        flash('Job not found!', 'error')

    return redirect(url_for('job_detail', job_id=job_id))

@app.route('/jobs/<int:job_id>/delete', methods=['POST'])
def delete_job(job_id):
    """Delete a job application"""
    if 0 <= job_id < len(job_list):
        deleted_job = job_list.pop(job_id)
        save_jobs_to_file(job_list)
        flash(f'Job application for {deleted_job.company} deleted successfully!', 'success')
    else:
        flash('Job not found!', 'error')
    
    return redirect(url_for('view_jobs'))

@app.route('/update-status')
def update_status_page():
    """Page for updating job application statuses"""
    return render_template('update_status.html', jobs=job_list)

@app.route('/search')
def search_jobs():
    """Search job applications"""
    search_type = request.args.get('type', '')
    keyword = request.args.get('keyword', '').lower()

    if not keyword:
        return render_template('search.html', jobs=[], search_results_with_index=[], search_type=search_type, keyword=keyword, job_list=job_list)

    search_results = []
    search_results_with_index = []

    if search_type == 'company':
        for i, job in enumerate(job_list):
            if keyword in job.company.lower():
                search_results.append(job)
                search_results_with_index.append((job, i))
    elif search_type == 'domain':
        for i, job in enumerate(job_list):
            if keyword in job.job_role.domain.lower():
                search_results.append(job)
                search_results_with_index.append((job, i))
    elif search_type == 'status':
        for i, job in enumerate(job_list):
            if keyword in job.status.lower():
                search_results.append(job)
                search_results_with_index.append((job, i))

    return render_template('search.html', jobs=search_results, search_results_with_index=search_results_with_index, search_type=search_type, keyword=keyword, job_list=job_list)

# API endpoints for AJAX requests
@app.route('/api/jobs')
def api_jobs():
    """API endpoint to get all jobs as JSON"""
    return jsonify([job.to_dict() for job in job_list])

@app.route('/api/stats')
def api_stats():
    """API endpoint to get job statistics"""
    stats = {}
    for job in job_list:
        status = job.status
        stats[status] = stats.get(status, 0) + 1
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
