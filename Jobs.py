class JobRole:
    def __init__ (self,domain, position, experience, tech_needed):
        self.domain = domain
        self.position= position
        self.experince= experience
        self.tech_needed = tech_needed

    def __str__(self):
        return f"{self.domain} | {self.position} | {self.experince} | {self.tech_needed}"

class JobApplication:
    status_options= {"Applied","Shortlisted","Rejected","Interviewed","Offer"}
    def __init__(self, company, date_applied, job_role, resume_version, notes):
        self.company= company
        self.date_applied= date_applied
        self.job_role= job_role
        self.resume_version = resume_version
        self.status = "Applied"  # Possible values: Applied, Rejected, Interviewed, Offer
        self.status_change= {self.status:{
            "notes": notes,
            "interview_scheduled": None ,
            "rounds_cleared": []
            }}
        

    def update_status (self, status, interview_scheduled=None, notes="", round_cleared=None):
        if status not in self.status_options:
            raise ValueError(f"Status must be one of the following {self.status_options}")
        self.status= status
        if status not in self.status_change:
            self.status_change[status]={
            "notes": notes,
            "interview_scheduled": None ,
            "rounds_cleared": []
            }
        else:
            self.status_change[status]['interview_scheduled']= interview_scheduled
            self.status_change[status]['notes']=notes
            self.status_change[status]['rounds_cleared'].append(round_cleared)

    def summary(self):
        return{
            "Company": self.company,
            "Date Applied" : self.date_applied,
            "Job Role": str(self.job_role),
            "Resume Version": self.resume_version,
            "Status": self.status,
            "Notes": self.status_change [self.status]['notes'],
            "Interview Scheduled": self.status_change[self.status]['interview_scheduled'],
            "Rounds Cleared": self.status_change[self.status]['rounds_cleared']
        }

def todict(self):
    return {
            "company": self.company,
            "date_applied" : self.date_applied,
            "job_role": {
                "domain" : self.job_role.domain,
                "position": self.job_role.position,
                "experience": self.job_role.experience,
                "tech_needed": self.job_role.tech_needed
            },
            "resume_version": self.resume_version,
            "status": self.status,
            "notes": self.status_change [self.status]['notes'],
            "interview_scheduled": self.status_change[self.status]['interview_scheduled'],
            "rounds_cleared": self.status_change[self.status]['rounds_cleared']
        }
    
@staticmethod
def from_dict(data):
    role_data= data["job_role"]
    role= JobRole( domain = role_data["domain"],
        positon = role_data["position"],
        experience = role_data["experience"],
        tech_needed = role_data["tech_needed"]
        )
    job = JobApplication( company= data["company"],
        date_applied=data["date_applied"],
        job_role=role,
        resume_version=data["resume_version"],
        notes="")
    job.status = data["status"]
    job.status_change[job.status]['notes'] = data["notes"]
    job.status_change[job.status]['interview_scheduled'] = data["interview_scheduled"]
    job.status_change[job.status]['rounds_cleared'] = data["rounds_cleared"]
    return job


        
if __name__== "__main__":
    job_role=JobRole(domain = "AI.Cloud projects", position= "Database Administrator", experience="4-10 Years", tech_needed=" Azure " )
    job1= JobApplication(
        company="TCS", 
        date_applied="2025-07-10",
        job_role=job_role, 
        resume_version="Resume with Projects and Non Tech Data" ,
        notes="Had interest in Cloud tech"
        )
    
    job1.update_status(status="Shortlisted", interview_scheduled="2025-07-12", notes="Hr has considered my whole experience" ,round_cleared="Online Screening")
    job1.update_status(status="Rejected", notes="No experince in Azure", round_cleared="HR Screening")
    
    print(job1.summary()) 
 