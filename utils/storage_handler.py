import json,os
from models.job_application import JobApplication

DATA_FILE = "job_data.json"

def load_jobs_from_file():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r") as text_wrapper: 
            content = text_wrapper.read().strip()
            if content:
                job_data=json.loads(content)
                return [JobApplication.from_dict(job) for job in job_data]
    return

def save_jobs_to_file(job_list):
    with open(DATA_FILE,'w') as f:
        json.dump([job.to_dict() for job in job_list],f, indent= 4 )