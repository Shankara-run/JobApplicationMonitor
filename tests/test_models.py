import unittest
from models.job_application import JobApplication
from models.job_role import JobRole

class TestModels(unittest.TestCase):
    def setUp(self):
        self.role = JobRole("AI","ML Engineer","2-4 years","python, tensorflow")
        self.app = JobApplication("openAI","2025-07-12",self.role,"Version made for AI","Interest in AI")
        self.app.status_change= {"Applied":{"notes":"Unable to get in","interview_scheduled":None,"rounds_cleared": ["HR","Online"]}}

    def test_role_summary(self):
        summary = self.role.summary()
        self.assertEqual(summary ["Domain"],"AI")
        self.assertIn("python",summary["Tech Needed"])
        self.assertIsInstance(summary["Tech Needed"], list)
    
    def test_app_summary(self):
        summary = self.app.summary()
        self.assertEqual(summary["Company"],"openAI")
        self.assertIn("python",summary["Job Role"]["Tech Needed"])

    def test_update_status(self):
        status_change = self.app.status_change
        self.assertEqual(status_change["Applied"]["notes"],"Unable to get in")
        self.assertIn("HR",status_change["Applied"]["rounds_cleared"])
        self.assertIsInstance(status_change["Applied"]["rounds_cleared"],list)
        self.assertIsInstance(status_change,dict)


    if __name__=="__main__":
        unittest.main()
