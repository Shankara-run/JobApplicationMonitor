
def get_new_job_details():
    print("Enter the Application details")
    company= input("Company Name :")
    date_applied= input("Date Applied (YYYY-DD-MM) :")
    domain = input("Domain (eg AI, Web, Cloud ) :")
    position = input("Position :")
    experience= input("Experience required (eg 2-4 years) :") 
    tech_needed= input("Tech stack (comma seperated) :")
    resume_version= input("Details of the Resume version used :")
    notes= input("Why have you applied for this role :")

    return { 
        "company": company,
        "date_applied": date_applied,
        "job_role": {
            "domain": domain,
            "position" : position,
            "experience": experience,
            "tech_needed": tech_needed,
            },
        "resume_version": resume_version,
        "notes": notes
    }

def no_applications_found():
    print("No Applications were found ")

def show_message(message):
    print(message)

def display_status_map(status_map):
     print("The Status Values are")
     for key, value in status_map.items():
        print(f"{key}: {value} ")

def get_status_change_details():
    notes= input(" Notes on  status change :")
    rounds_cleared = [round.strip() for round in input("Rounds cleared (comma separated): ").split(",") if round.strip()]
    interview_scheduled = input("Interview scheduled date (leave blank if not applicable) : ") or None
    return{
        "notes": notes,
        "rounds_cleared": rounds_cleared,
        "inteview_scheduled": interview_scheduled
    }
    
def display_job_summary (index, summary_dict):
    print(f"Details of the job #{index+1}")
    for key, value in summary_dict.items():
        print(f"{key}: {value} ")

def display_short_summary (company_name_list):
    print(" Avalaible job applications :")
    for index, company_name in enumerate(company_name_list):
        print(f" {index+1}: {company_name}")

def get_choice():
    return input (f"Enter the number of your choice :")

def invalid_choice():
    print("Please enter a valid number")

def get_input(message):
    
    return input(message)

def get_jobs_by_category():
    print("\n Search by")
    print("1. Company name")
    print("2. Domain name (eg AI, Cloud)")
    print("3. Status")
    try:
        choice = int(input("Enter the choice (1-3): "))
        if choice in [1, 2, 3]:
            return choice
        else:
            print("Please choose a valid number between 1 and 3.")
            return None
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.")
        return None
    
def show_menu():
    print("\n Job application tracker")
    print("1. Add a new job that you have applied")
    print("2. View Application Details")
    print("3. Change Application Status ")
    print("4. Delete Application details")
    print("5. Application summary")
    print("6. Search for Application")
    print("7. Exit window")

    