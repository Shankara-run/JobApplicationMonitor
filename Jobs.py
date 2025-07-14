class JobRole:
    def __init__ (self,domain, position, experience, tech_needed):
        self.domain = domain
        self.position= position
        self.experince= experience
        self.tech_needed = tech_needed

    def __str__(self):
        return f"{self.domain} | {self.position} | {self.experince} | {self.tech_needed}"

class JobApplication:
    status_options= {"Applied","Rejected","Interviewed","Offer"}
    def __init__(self, company, date_applied, job_role, resume_version):
        self.company= company
        self.date_applied= date_applied
        self.job_role= job_role
        self.resume_version = resume_version
        self.status = "Applied"  # Possible values: Applied, Rejected, Interviewed, Offer
        self.interview_scheduled = None
        self.notes= {self.status:""}
        self.rounds_cleared =  []
        
    def update_status (self, status, interview_scheduled=None, note="", round_cleared=None):
        if status not in self.status_options:
            raise ValueError(f"Status must be one of the following {self.status_options}")
        self.status= status
        if interview_scheduled:
            self.interview_scheduled= interview_scheduled
        self.notes[status]=note
        if round_cleared:
           self.rounds_cleared.append(round_cleared)

    def summary(self):
        return{
            "Company": self.company,
            "Date Applied" : self.date_applied,
            "Job Role": str(self.job_role),
            "Resume Version": self.resume_version,
            "Status": self.status,
            "Notes": self.notes,
            "Interview Scheduled": self.interview_scheduled,
            "Rounds Cleared": self.rounds_cleared
        }

        
if __name__== "__main__":
    job_role=JobRole(domain = "AI.Cloud projects", position= "Database Administrator", experience="4-10 Years", tech_needed=" Azure " )
    job1= JobApplication(
        company="TCS", 
        date_applied="2025-07-10",
        job_role=job_role, 
        resume_version="Resume with Projects and Non Tech Data" 
        )
    
    job1.update_status(status="Applied",interview_scheduled="2025-07-12", note="Had interest in Cloud tech", round_cleared="Online Screening")
    job1.update_status(status="Rejected", note="No experince in Azure", round_cleared="HR Screening")
    
    print(job1.summary()) 
 