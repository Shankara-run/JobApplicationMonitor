from Jobs import JobApplication,JobRole
import json,os
DATA_FILE = "job_data.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE,"r") as text_wrapper: 
        content = text_wrapper.read().strip()
        if content:
            job_data=json.loads(content)
            job_list=[JobApplication.from_dict(job) for job in job_data]
        else:
            job_list=[]
else:
    job_list=[]

def save_jobs_to_file():
    with open(DATA_FILE,'w') as f:
        json.dump([job.to_dict() for job in job_list],f, indent= 4 )
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
    save_jobs_to_file()
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
    index=int(input(f"Enter the choice in number :"))-1
    if 0<= index <= len(job_list):
        company= job_list[index].company
    else:
        print ("Invalid Choice")
        return
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
    notes= input(" Notes on  status change :")
    rounds_cleared = [round.strip() for round in input("Rounds cleared (comma separated): ").split(",") if round.strip()]
    interview_scheduled = input("Interview scheduled date (leave blank if not applicable) : ") or None
    status_change={status:{ "notes":notes,
        "interview_scheduled":interview_scheduled,
        "rounds_cleared":rounds_cleared}}
    job_needs_update.update_status(status_change)
    save_jobs_to_file()

    print("Status updated successfully.")
    
if __name__=="__main__":
    main()
