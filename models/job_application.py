from models.job_role import JobRole

class JobApplication:
    
    status_map = {
        "1": "Applied",
        "2": "Shortlisted",
        "3": "Interviewed",
        "4": "Rejected",
        "5": "Offer"
    } 
    def __init__(self,company, date_applied, job_role, resume_version, notes):
        self.company= company
        self.date_applied= date_applied
        self.job_role=  job_role
        self.resume_version = resume_version
        self.status = "Applied"  # Possible values: Applied, Rejected, Interviewed, Offer
        self.status_change= {self.status:{
            "notes": notes,
            "interview_scheduled": None ,
            "rounds_cleared": []
        }}

    def update_status(self, status_change):
        if not isinstance(status_change, dict):
            raise ValueError("status_change must be a dictionary.")

        for status, details in status_change.items():
            if status not in self.status_map.values():
             raise ValueError(f"Invalid status: {status}. Must be one of: {self.status_options}")
        
            self.status = status  # set current status
            
            self.status_change[status] = {
            "notes": details.get("notes", ""),
            "interview_scheduled": details.get("interview_scheduled", None),
            "rounds_cleared": details.get("rounds_cleared", [])
        }
  
    
    def summary(self):
        return{
            "Company": self.company,
            "Date Applied" : self.date_applied,
            "Job Role": self.job_role.summary(),
            "Resume Version": self.resume_version,
            "Status": self.status,
            "Status Changes": self.status_change
        }

    def to_dict(self):
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
            "status_change": self.status_change,
            
        }
    
    @staticmethod
    def from_dict(data):
        role_data= data["job_role"]
        role= JobRole( domain = role_data["domain"],
        position = role_data["position"],
        experience = role_data["experience"],
        tech_needed = role_data["tech_needed"]
        )
        job = JobApplication( company= data["company"],
        date_applied=data["date_applied"],
        job_role=role,
        resume_version=data["resume_version"],
        notes="")
        job.status = data["status"]
        job.status_change= data.get("status_change",'{}')
        return job
    