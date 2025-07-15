from Jobs import JobApplication,JobRole
job_list=[]

def show_menu():
    print("\n Job application tracker")
    print("1. Add a new job that you have applied")
    print("2. View Jobs Details")
    print("3. Change Job Status ")
    print("4. Exit tracker")

def main():
    while True:
        show_menu()
        choice = input("Enter your Choice : ")
        if choice=='1':
            add_new_job()
        elif choice=='2':
            view_jobs()
        elif choice=='3':
            update_status()
        elif choice=='4':
            print("Exiting Tracker")
            break
        else:
            print("Invalid Choice")
    

def add_new_job():
    company= input("Company Name :")
    date_applied= input("Date Applied (YYYY-DD-MM) :")
    domain = input("Domain (eg AI, Web, Cloud ) :")
    position = input("Position :")
    experience= input("Experience required (eg 2-4 years) :") 
    tech_needed= input("Tech stack (comma seperated) :")
    resume_version= input("Details of the Resume version used :")
    notes= input("Why have you applied for this role :")
    role= JobRole(domain, position, experience, tech_needed)
    job= JobApplication(company, date_applied, role, resume_version,notes)
    
    job_list.append(job)
    print(f"Job application details at {company} added successfully")


def view_jobs():
    if not job_list:
        print("No Applications were found")
        return
    for index,job in enumerate(job_list):
        print  (f"Details of the Job#{index+1}")
        for key,value in job.summary().items():
            print(f"{key} : {value}")

def update_status():
    if not job_list:
        print("No Applications were found")
    
    print("job application details ")
    for index,job in enumerate(job_list):
        print(f" {index+1}: {job.company}")
    company=input(f"Enter the company Name :")

    job_needs_update= None
    for job in job_list:
        if job.company.lower()== company.lower():
            job_needs_update= job
            break
    if not job_needs_update:
        print("No job found for the given company.")
        return
    
    print("Enter the Status change for the application : \n 1. Shortlisted\n 2. Inteviewed\n 3. Rejected\n 4. Offer \n")
    status_map = {
        "1": "Shortlisted",
        "2": "Interviewed",
        "3": "Rejected",
        "4": "Offer"
    }    
    status=status_map.get(input("Status (1-4) :"))
    if not status:
        print("Invalid status selection.")
        return
    notes= input(" Notes on  status change:")
    round_cleared= input(" Round cleared comma seperated")
    interview_scheduled = input("Interview scheduled date (leave blank if not applicable): ") or None
    job_needs_update.update_status(status,notes,interview_scheduled,round_cleared)
    print("Status updated successfully.")
    
if __name__=="__main__":
    main()
