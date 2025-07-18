from models.job_application import JobApplication
from models.job_role import JobRole
from utils.storage_handler import save_jobs_to_file as save , load_jobs_from_file as load
from interface.cli_interface import get_input,get_jobs_by_category, get_status_change_details,display_status_map, display_short_summary, display_job_summary, show_message, get_new_job_details, no_applications_found, get_choice,invalid_choice
job_list = load()

def add_new_job():
    details = get_new_job_details()
    role= JobRole(
        domain= details["job_role"]["domain"], 
        position= details["job_role"]["position"], 
        experience= details["job_role"]["experience"], 
        tech_needed= details ["job_role"]["tech_needed"]
        )
    job= JobApplication(
        company= details["company"],
        date_applied= details["date_applied"], 
        job_role=role, 
        resume_version= details["resume_version"],
        notes= details["notes"]
        )
    job_list.append(job)
    save(job_list)
    show_message(f"Job application details at {job.company} added successfully")


def view_jobs():
    if not job_list:
        no_applications_found()
        return
    for index,job in enumerate(job_list):
        display_job_summary (index, job.summary())



def delete_job():
    if not job_list:
        show_message("No Job Applications were found")
        return
    display_short_summary (job.company for job in job_list )
   
    try:
        index=int(get_choice())-1
        if 0<=index<=len(job_list):
            deleted_job= job_list.pop(index)
            save(job_list)
            show_message(f"The job applications details of the company {deleted_job.company} has been deleted successfully ")
        else:
           invalid_choice()
    except ValueError:
        invalid_choice()


def update_status():
    if not job_list:
        no_applications_found()
    display_short_summary(job.company for job in job_list)
    try:
        index=int(get_choice())-1
        if 0<= index <= len(job_list):
            company= job_list[index].company
        else:
            invalid_choice()
    except ValueError:
        invalid_choice()

    job_needs_update= None
    for job in job_list:
        if job.company.lower()== company.lower():
            job_needs_update= job
            break
    if not job_needs_update:
        no_applications_found()
        return
    display_status_map(job_needs_update.status_map)      
    status=job_needs_update.status_map.get(get_choice())
    if not status:
        invalid_choice()
        return
    status_change={status:get_status_change_details()}
    job_needs_update.update_status(status_change)
    save(job_list)

    print("Status updated successfully.")

def summary_count():
    summary_count={}
    for job in job_list:
        status= job.status
        summary_count[status]= summary_count.get(status,0)+1 
        #Look in the status_summary dictionary for this status.
        #If it's not there yet, just use 0.
    for key, value in summary_count.items():
        print(f"{key}: {value} application(s) ")
        
def search_jobs():

    choice=get_jobs_by_category()
    
    if choice == 1:
        keyword= get_input("Enter the company name :").lower()
        search_list= [jobs for jobs in job_list if keyword in jobs.company.lower()]

    elif choice == 2:
        keyword= get_input("Enter the domain name (eg. AI, Cloud) :").lower()
        search_list= [jobs for jobs in job_list if keyword in jobs.job_role.domain.lower()]

    elif choice == 3:
        keyword= get_input("Enter the status (eg. Applied, Interviewed) :").capitalize()
        search_list= [jobs for jobs in job_list if keyword in jobs.status]
    
    else:
        invalid_choice()
        return
    if search_list:
        display_short_summary(job.company for job in search_list)
        for index, job in enumerate(search_list):
         display_job_summary(index, job.summary())
    else:
        no_applications_found()