# Job Application Monitor - Web Frontend

A modern web-based frontend for the Job Application Monitor system, built with Flask and Bootstrap.

## Features

### 🎯 Dashboard
- **Overview Statistics**: Total applications, status breakdown with visual progress bars
- **Recent Applications**: Quick view of the latest 5 job applications
- **Quick Actions**: Easy access to add new jobs, view all jobs, and search

### 📋 Job Management
- **Add New Jobs**: Comprehensive form to add job applications with company details, job role information, and application notes
- **View All Jobs**: Tabular view of all job applications with sorting and filtering
- **Job Details**: Detailed view of individual job applications with complete information
- **Quick Status Updates**: Update job status directly from any page with modal dialogs
- **Dedicated Update Status Page**: Centralized page for bulk status updates with filtering
- **Status History**: Timeline view of all status changes with detailed notes
- **Delete Jobs**: Safe deletion with confirmation dialogs

### 🔍 Search & Filter
- **Multi-criteria Search**: Search by company name, domain, or status
- **Real-time Results**: Instant search results with highlighting
- **Quick Search Suggestions**: Pre-defined search buttons for common queries

### 📱 Responsive Design
- **Mobile-First**: Fully responsive design that works on all devices
- **Modern UI**: Clean, professional interface with Bootstrap 5
- **Interactive Elements**: Hover effects, animations, and smooth transitions

## Technology Stack

- **Backend**: Flask 2.3.3
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **UI Framework**: Bootstrap 5.3.0
- **Icons**: Bootstrap Icons
- **Data Storage**: JSON file-based storage (existing system)

## Installation & Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python app.py
   ```

3. **Access the Web Interface**:
   Open your browser and navigate to `http://localhost:5000`

## File Structure

```
JobApplicationMonitor/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── dashboard.html    # Dashboard page
│   ├── jobs.html         # All jobs listing
│   ├── add_job.html      # Add new job form
│   ├── job_detail.html   # Individual job details
│   └── search.html       # Search interface
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Custom CSS styles
│   └── js/
│       └── main.js       # JavaScript functionality
├── models/               # Data models (existing)
├── controllers/          # Business logic (existing)
├── utils/                # Utility functions (existing)
└── interface/            # CLI interface (existing)
```

## Key Features Explained

### Dashboard
- **Statistics Cards**: Visual representation of application counts by status
- **Progress Bars**: Show distribution of applications across different statuses
- **Recent Activity**: Quick access to recently added applications

### Job Management
- **Form Validation**: Client-side and server-side validation for all forms
- **Status Timeline**: Visual timeline showing the progression of each application
- **Multiple Update Options**: Update status from dashboard, jobs list, search results, or dedicated update page
- **Modal Dialogs**: Quick status updates without leaving the current page
- **Status Filtering**: Filter applications by status on the update page
- **Smart Redirects**: Automatically return to the previous page after status updates

### Search Functionality
- **Flexible Search**: Search across company names, domains, and statuses
- **Result Highlighting**: Search terms are highlighted in results
- **Filter Options**: Additional filtering capabilities for refined searches

### User Experience
- **Flash Messages**: User feedback for all actions (success/error messages)
- **Confirmation Dialogs**: Safe deletion with confirmation modals
- **Loading States**: Visual feedback during form submissions
- **Keyboard Navigation**: Full keyboard accessibility support

## API Endpoints

The application also provides REST API endpoints:

- `GET /api/jobs` - Get all jobs as JSON
- `GET /api/stats` - Get application statistics

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Development Notes

- The web frontend integrates seamlessly with the existing CLI application
- All existing data models and business logic are preserved
- The JSON data file remains the single source of truth
- No database migration required - works with existing data

## Future Enhancements

- Export functionality (PDF, Excel)
- Advanced filtering and sorting options
- Data visualization charts
- Email notifications for status changes
- Calendar integration for interview scheduling
- Bulk import/export capabilities

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is part of the Job Application Monitor system.
