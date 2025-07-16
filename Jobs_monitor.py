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

def delete_job():
    if not job_list:
        print("No Job Applications were found")
        return
    for index, job in enumerate(job_list, start=1):
        print (f"{index}. {job.company}")
    try:
        index=int(input(f"Enter you choice 1-{len(job_list)} :"))-1
        if 0<=index<=len(job_list):
            deleted_job= job_list.pop(index)
            save_jobs_to_file()
            print(f"The job applications details of the company {deleted_job.company} has been deleted successfully ")
        else:
           print("Invalid index")
    except ValueError:
        print("Please enter a valid number")


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
    print("\n Search by")
    print("1. Company name")
    print("2. Domain name (eg AI, Cloud)")
    print("3. Status")
    choice= int(input("Enter the choice (1-3) :"))
    
    if choice == 1:
        keyword= input("Enter the company name :").lower()
        search_list= [jobs for jobs in job_list if keyword in jobs.company.lower()]

    elif choice == 2:
        keyword= input("Enter the domain name (eg. AI, Cloud) :").lower()
        search_list= [jobs for jobs in job_list if keyword in jobs.job_role.domain.lower()]

    elif choice == 3:
        keyword= input("Enter the status (eg. Applied, Interviewed) :").capitalize()
        search_list= [jobs for jobs in job_list if keyword in jobs.status]
    
    else:
        print("Invalid Choice")
        return
    if search_list:
        for index, job in enumerate(search_list, start=1):
            print(f" \nSearch result #{index}")
            for key, value in job.summary().items():
                print(f"{key}: {value}")
    else:
        print("No matching application was found ")
    


def show_menu():
    print("\n Job application tracker")
    print("1. Add a new job that you have applied")
    print("2. View Application Details")
    print("3. Change Application Status ")
    print("4. Delete Application details")
    print("5. Application summary")
    print("6. Search for Application")
    print("7. Exit window")

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
            delete_job()
        elif choice=='5':
            summary_count()
        elif choice=='6':
            search_jobs()
        elif choice=='7':
            print("Exiting Tracker")
            break
        else:
            print("Invalid Choice")
    
if __name__=="__main__":
    main()
