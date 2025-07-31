// Main JavaScript file for Job Application Monitor

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Form validation enhancement
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Real-time search functionality
    const searchInput = document.getElementById('keyword');
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                // Could implement live search here
                console.log('Search term:', this.value);
            }, 300);
        });
    }

    // Dynamic status badge colors
    updateStatusBadges();

    // Initialize dashboard charts if on dashboard page
    if (document.querySelector('.dashboard-stats')) {
        initializeDashboardCharts();
    }
});

// Function to update status badge colors dynamically
function updateStatusBadges() {
    const statusBadges = document.querySelectorAll('.status-badge');
    statusBadges.forEach(badge => {
        const status = badge.textContent.trim().toLowerCase();
        badge.classList.remove('bg-success', 'bg-info', 'bg-warning', 'bg-primary', 'bg-danger');
        
        switch(status) {
            case 'applied':
                badge.classList.add('bg-success');
                break;
            case 'shortlisted':
                badge.classList.add('bg-info');
                break;
            case 'interviewed':
                badge.classList.add('bg-warning');
                break;
            case 'offer':
                badge.classList.add('bg-primary');
                break;
            case 'rejected':
                badge.classList.add('bg-danger');
                break;
            default:
                badge.classList.add('bg-secondary');
        }
    });
}

// Function to initialize dashboard charts (placeholder for future enhancement)
function initializeDashboardCharts() {
    // This could be enhanced with Chart.js or similar library
    console.log('Dashboard charts initialized');
}

// Utility function to format dates
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
}

// Function to show loading spinner
function showLoading(element) {
    const spinner = document.createElement('div');
    spinner.className = 'spinner-border spinner-border-sm me-2';
    spinner.setAttribute('role', 'status');
    element.prepend(spinner);
    element.disabled = true;
}

// Function to hide loading spinner
function hideLoading(element) {
    const spinner = element.querySelector('.spinner-border');
    if (spinner) {
        spinner.remove();
    }
    element.disabled = false;
}

// AJAX helper function
async function makeRequest(url, options = {}) {
    try {
        const response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('Request failed:', error);
        throw error;
    }
}

// Function to refresh dashboard stats (for future AJAX implementation)
async function refreshDashboardStats() {
    try {
        const stats = await makeRequest('/api/stats');
        updateDashboardStats(stats);
    } catch (error) {
        console.error('Failed to refresh stats:', error);
    }
}

// Function to update dashboard stats display
function updateDashboardStats(stats) {
    Object.entries(stats).forEach(([status, count]) => {
        const element = document.querySelector(`[data-status="${status}"] .card-title`);
        if (element) {
            element.textContent = count;
        }
    });
}

// Enhanced form validation
function validateJobForm(form) {
    const requiredFields = form.querySelectorAll('[required]');
    let isValid = true;
    const errors = [];

    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            field.classList.add('is-invalid');
            errors.push(`${field.labels[0]?.textContent || field.name} is required`);
            isValid = false;
        } else {
            field.classList.remove('is-invalid');
        }
    });

    // Validate date format
    const dateField = form.querySelector('input[type="date"]');
    if (dateField && dateField.value) {
        const selectedDate = new Date(dateField.value);
        const today = new Date();
        if (selectedDate > today) {
            dateField.classList.add('is-invalid');
            errors.push('Application date cannot be in the future');
            isValid = false;
        }
    }

    // Show errors if any
    if (!isValid) {
        showFormErrors(errors);
    }

    return isValid;
}

// Function to show form errors
function showFormErrors(errors) {
    const errorContainer = document.getElementById('form-errors');
    if (errorContainer) {
        errorContainer.innerHTML = errors.map(error => 
            `<div class="alert alert-danger">${error}</div>`
        ).join('');
    } else {
        alert('Please fix the following errors:\n' + errors.join('\n'));
    }
}

// Function to clear form errors
function clearFormErrors() {
    const errorContainer = document.getElementById('form-errors');
    if (errorContainer) {
        errorContainer.innerHTML = '';
    }
}

// Export functions for use in other scripts
window.JobMonitor = {
    updateStatusBadges,
    formatDate,
    showLoading,
    hideLoading,
    makeRequest,
    refreshDashboardStats,
    validateJobForm,
    clearFormErrors
};
