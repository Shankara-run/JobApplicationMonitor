import os
import unittest

from models.job_role import JobRole
from models.job_application import JobApplication
from utils.storage_handler import save_jobs_to_file, load_jobs_from_file

class TestStorageHandler(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_job_data.json"
        role = JobRole("AI", "Data Scientist", "3 years", ["Python", "SQL"])
        self.job = JobApplication("TestCorp", "2025-07-01", role, "v1", "Initial stage")
        self.job_list = [self.job]

    def tearDown(self):
        # Remove test file after each test to keep things clean
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load_jobs(self):
        save_jobs_to_file(self.job_list, self.test_file)
        loaded_jobs = load_jobs_from_file(self.test_file)

        self.assertEqual(len(loaded_jobs), 1)
        self.assertEqual(loaded_jobs[0].company, "TestCorp")
        self.assertEqual(loaded_jobs[0].job_role.domain, "AI")
        self.assertEqual(loaded_jobs[0].job_role.tech_needed, ["Python", "SQL"])

if __name__ == '__main__':
    unittest.main()