import unittest
import requests
import json
import subprocess
import os

BASE_URL = "http://127.0.0.1:5000/api/"

null_device = "nul" if os.name == "nt" else "/dev/null"

class TestApp(unittest.TestCase):
    """To be used for tests that do not modify the database."""
    pass

class TestAppModDB(unittest.TestCase):
    """To be used for tests that modify the database."""
    def tearDown(self):
        # reset database and redirects output to null device to not flood terminal
        with open(null_device, 'w') as devnull:
            subprocess.run("python load_init_sql.py", shell=True, cwd="../..", stdout=devnull, stderr=subprocess.STDOUT)

# # GET requests; 22 tests.
class TestSkill(TestApp):
    # test for getAllSkills.py
    def test_getAllSkills(self):
        response = requests.get(BASE_URL + "allskills").status_code
        expected = 200
        self.assertEqual(response, expected)

class TestApplicant(TestApp):
    # test for getApplicants.py
    def test_getApplicants(self):
        response = requests.get(BASE_URL + "applicants?lid=1").json()
        print(response)
        expected = {
                        "Applicants": [
                            {
                                "Application_ID": 1,
                                "Dept": "Sales",
                                "Email": "Derek.Tan@allinone.com.sg",
                                "Name": "Derek Tan",
                                "Staff_ID": 140001
                            },
                            {
                                "Application_ID": 2,
                                "Dept": "Sales",
                                "Email": "Susan.Goh@allinone.com.sg",
                                "Name": "Susan Goh",
                                "Staff_ID": 140002
                            }
                        ]
                    }
        self.assertEqual(response, expected)

    def test_getApplicantsInvalid(self):
        response = requests.get(BASE_URL + "applicants?lid=-1").json()
        expected = {
                        "Applicants": []
                    }
        self.assertEqual(response, expected)

class TestRoleListing(TestApp):
    # test for getRoleListings.py
    def test_getRoleListings(self):
        response = requests.get(BASE_URL + "rolelistings?staff_ID=130001").status_code
        expected = 200
        self.assertEqual(response, expected)

    def test_getRoleListingsInvalid(self):
        response = requests.get(BASE_URL + "rolelistings?staff_ID=-1").json()
        expected = {
                        "error": "'Staff Matched Skills'"
                    }
        self.assertEqual(response, expected)

class TestRole(TestApp):
    # test for getRoles.py
    def test_getRoles(self):
        response = requests.get(BASE_URL + "roles").status_code
        expected = 200
        self.assertEqual(response, expected)

    # test for getRoleDesc.py
    def test_getRoleDesc(self):
        response = requests.get(BASE_URL + "roledesc?role_name=Admin%20Executive").json()
        expected = {
                        "Description": "Admin Executive will act as the point of contact for all employees, providing administrative support and managing their queries. Main duties include managing office stock, preparing regular reports (e.g. expenses and office budgets) and organizingï¿½company records. If you have previous experience as anï¿½Office Administratorï¿½or similar administrative role, weï¿½d like to meet you. "
                    }
        self.assertEqual(response, expected)

    def test_getRoleDescInvalid(self):
        response = requests.get(BASE_URL + "roledesc?role_name=Admin%20Executiv").json()
        expected = {
                        "error": "Invalid role name."
                    }
        self.assertEqual(response, expected)

    # test for getAvailableRoles.py
    def test_getAvailableRoles(self):
        response = requests.get(BASE_URL + "availableroles").status_code
        expected = 200
        self.assertEqual(response, expected)

class TestRoleSkill(TestApp):
    # test for getRoleSkills.py
    def test_getRoleSkills(self):
        response = requests.get(BASE_URL + "roleskills?rolename=Admin%20Executive").json()
        expected = {
                        "Role Skills": [
                            "Collaboration",
                            "Communication",
                            "Customer Relationship Management",
                            "Problem Solving",
                            "Solutions Design Thinking",
                            "Stakeholder Management",
                            "Technology Integration"
                        ]
                    }
        self.assertEqual(response, expected)

    def test_getRoleSkillsInvalid(self):
        response = requests.get(BASE_URL + "roleskills?rolename=Admin%20Executiv").json()
        expected = {
                        "error": "Invalid role name. Role not found!"
                    }
        self.assertEqual(response, expected)

class TestRoleSkillMatch(TestApp):
        # test for getAllRoleSkillMatch.py
    def test_getAllRoleSkillMatch(self):
        response = requests.get(BASE_URL + "allroleskillmatch?lid=1").json()
        expected = {
                        "Applicants": [
                            {
                                "Application ID": 1,
                                "Percentage Match": "30.77",
                                "Staff Dept": "Sales",
                                "Staff ID": 140001,
                                "Staff Matched Skills": [
                                    "Account Management",
                                    "Business Development",
                                    "Pricing Strategy",
                                    "Product Management"
                                ],
                                "Staff Mismatched Skills": [
                                    "Customer Acquisition Management",
                                    "Database Administration",
                                    "Financial Statements Analysis",
                                    "Technology Integration"
                                ],
                                "Staff Name": "Derek Tan"
                            },
                            {
                                "Application ID": 2,
                                "Percentage Match": "0.0",
                                "Staff Dept": "Sales",
                                "Staff ID": 140002,
                                "Staff Matched Skills": [],
                                "Staff Mismatched Skills": [
                                    "Accounting and Tax Systems",
                                    "Business Environment Analysis",
                                    "Customer Relationship Management",
                                    "Professional and Business Ethics"
                                ],
                                "Staff Name": "Susan Goh"
                            }
                        ]
                    }
        self.assertEqual(response, expected)
    
    def test_getAllRoleSkillMatchInvalid(self):
        response = requests.get(BASE_URL + "allroleskillmatch?lid=100").json()
        expected = {
                        "error": "Invalid role name. Role not found!"
                    }
        self.assertEqual(response, expected)

    # test for getRoleSkillMatch.py
    def test_getRoleSkillMatch(self):
        response = requests.get(BASE_URL + "roleskillmatch?sid=130001&rolename=Admin%20Executive").json()
        expected = {
                        "Percentage Match": "0.0",
                        "Staff Matched Skills": [],
                        "Staff Missing Skills": [
                            "Collaboration",
                            "Communication",
                            "Customer Relationship Management",
                            "Problem Solving",
                            "Solutions Design Thinking",
                            "Stakeholder Management",
                            "Technology Integration"
                        ]
                    }
        self.assertEqual(response, expected)

    def test_getRoleSkillMatchInvalid(self):
        response = requests.get(BASE_URL + "roleskillmatch?sid=1&rolename=Admin%20Executiv").json()
        expected = {
                        "error": "'Role Skills'"
                    }
        self.assertEqual(response, expected)

class TestUser(TestApp):
    # test for getUser.py
    def test_getUser(self):
        response = requests.get(BASE_URL + "user?email=jack.sim@allinone.com.sg").json()
        expected = {
                        "Country": "Singapore",
                        "Dept": "Chariman",
                        "Email": "jack.sim@allinone.com.sg",
                        "Role": 1,
                        "Staff_FName": "John",
                        "Staff_ID": 130001,
                        "Staff_LName": "Sim"
                    }
        self.assertEqual(response, expected)
    
    def test_getUserInvalid(self):
        response = requests.get(BASE_URL + "user?email=jac.sim@allinone.com.sg").json()
        expected = {
                        "error": "User not found"
                    }
        self.assertEqual(response, expected)

    # test for getUserByID.py
    def test_getUserByID(self):
        response = requests.get(BASE_URL + "userID?id=130001").json()
        expected = {
                        "Country": "Singapore",
                        "Dept": "Chariman",
                        "Email": "jack.sim@allinone.com.sg",
                        "Role": 1,
                        "Staff_FName": "John",
                        "Staff_ID": 130001,
                        "Staff_LName": "Sim"
                    }
        self.assertEqual(response, expected)

    def test_getUserByIDInvalid(self):
        response = requests.get(BASE_URL + "userID?id=13000").json()
        expected = {
                        "error": "User not found"
                    }
        self.assertEqual(response, expected)

    # test for getUsers.py
    def test_getUsers(self):
        response = requests.get(BASE_URL + "users").status_code
        expected = 200
        self.assertEqual(response, expected)

class TestStaffSkill(TestApp):
    # test for getStaffSkills.py
    def test_getStaffSkills(self):
        response = requests.get(BASE_URL + "staffskills?sid=140001").json()
        expected = {
                        "Staff Skills": [
                            "Account Management",
                            "Business Development",
                            "Customer Acquisition Management",
                            "Database Administration",
                            "Financial Statements Analysis",
                            "Pricing Strategy",
                            "Product Management",
                            "Technology Integration"
                        ]
                    }
        self.assertEqual(response, expected)

    def test_getStaffSkillsInvalid(self):
        response = requests.get(BASE_URL + "staffskills?sid=-1").json()
        expected = {
                        "error": "Invalid staff ID. Staff not found!"
                    }
        self.assertEqual(response, expected)

# POST requests; 9 tests.
class TestCreateRoleListing(TestAppModDB):
    # test for createRoleListing.py
    def test_createRoleListing(self):
        request_body = {'name': 'HR Director', 
                        'desc': "The HR Director is responsible for establishing the overall talent management strategies.", 
                        'deadline': '2023-11-31'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(BASE_URL + "createRoleListing",
                                 data=json.dumps(request_body),
                                 headers=headers).json()
        expected = {
                        'Status': 'Role Listing created successfully.'
                    }
        self.assertEqual(response, expected)

    def test_createRoleListingInvalidDeadline(self):
        request_body = {'name': 'Sales Manager', 
                        'desc': "Sales Manager test.", 
                        'deadline': '2020-10-31'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(BASE_URL + "createRoleListing",
                                 data=json.dumps(request_body),
                                 headers=headers).json()
        expected = {
                        'Status': 'Invalid deadline. Date has passed.'
                    }
        self.assertEqual(response, expected)

    def test_createRoleListingRoleExisting(self):
        request_body = {'name': 'Developer', 
                        'desc': "Developer test.", 
                        'deadline': '2023-10-31'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(BASE_URL + "createRoleListing",
                                 data=json.dumps(request_body),
                                 headers=headers).json()
        expected = {
                        'Status': 'Unavailable Role. There is an existing role listing open.'
                    }
        self.assertEqual(response, expected)

class TestUpdateRoleListing(TestAppModDB):
    # test for updateRoleListing.py
    def test_updateRoleListing(self):
        request_body = {
                        'lid': 4, 
                        'name': 'Consultancy Director', 
                        'desc': 'test', 
                        'deadline': '2023-12-30'
                        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(BASE_URL + "updateRoleListing",
                                 data=json.dumps(request_body),
                                 headers=headers).json()
        expected = {
                        'Status': 'Data updated successfully.'
                    }
        self.assertEqual(response, expected)

    def test_updateRoleListingInvalidlid(self):
        request_body = {
                        'lid': -1, 
                        'name': 'Consultancy Director', 
                        'desc': 'test', 
                        'deadline': '2023-12-30'
                        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(BASE_URL + "updateRoleListing",
                                 data=json.dumps(request_body),
                                 headers=headers).json()
        expected = {
                        'Status': 'Rolename or Listing ID invalid. Not found.'
                    }
        self.assertEqual(response, expected)

    def test_updateRoleListingInvalidDeadline(self):
        request_body = {
                        'lid': 4, 
                        'name': 'Consultancy Director', 
                        'desc': 'test', 
                        'deadline': '2020-12-30'
                        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(BASE_URL + "updateRoleListing",
                                 data=json.dumps(request_body),
                                 headers=headers).json()
        expected = {
                        'Status': 'Invalid deadline. Date has passed.'
                    }
        self.assertEqual(response, expected)

class TestUpdateStaffApplication(TestAppModDB):
    # test for updateStaffApplication.py
    def test_updateStaffApplication(self):
        response = requests.post(BASE_URL + "updateStaffApplication/1/130001").json()
        expected = {
                        "Status": "Data updated successfully."
                    }
        self.assertEqual(response, expected)

    def test_updateStaffApplicationInvalid(self):
        response = requests.post(BASE_URL + "updateStaffApplication/-1/140001").json()
        expected = {
                        "Status": "ListingID or StaffID invalid. Not found."
                    }
        self.assertEqual(response, expected)

    def test_updateStaffApplicationExists(self):
        response = requests.post(BASE_URL + "updateStaffApplication/1/140001").json()
        expected = {
                        "Status": "Staff and Listing combination already exists."
                    }
        self.assertEqual(response, expected)

if __name__ == '__main__':
    print("=== Unit Tests Started ===")
    unittest.main()
    print("=== Unit Tests Completed ===")
