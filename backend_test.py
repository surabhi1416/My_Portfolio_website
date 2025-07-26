#!/usr/bin/env python3
"""
Backend API Testing Suite for Portfolio Application
Tests all portfolio API endpoints for functionality and data integrity
"""

import requests
import json
import sys
from datetime import datetime
from typing import Dict, Any, List

# Backend URL from environment
BACKEND_URL = "https://f9ba1be0-f352-4977-94ab-a1c01fe87f50.preview.emergentagent.com"

class PortfolioAPITester:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.test_results = []
        
    def log_test(self, test_name: str, success: bool, message: str, details: Dict = None):
        """Log test results"""
        result = {
            "test": test_name,
            "success": success,
            "message": message,
            "timestamp": datetime.now().isoformat(),
            "details": details or {}
        }
        self.test_results.append(result)
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status}: {test_name} - {message}")
        if details and not success:
            print(f"   Details: {details}")
    
    def test_api_health_check(self):
        """Test 1: API Health Check - Test if backend is running properly"""
        try:
            # Test basic health endpoint
            response = self.session.get(f"{self.base_url}/api/health", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "healthy" and data.get("service") == "portfolio-api":
                    self.log_test("API Health Check", True, "Backend is running and healthy")
                    return True
                else:
                    self.log_test("API Health Check", False, "Health endpoint returned unexpected data", {"response": data})
                    return False
            else:
                self.log_test("API Health Check", False, f"Health endpoint returned status {response.status_code}", {"response": response.text})
                return False
                
        except requests.exceptions.RequestException as e:
            self.log_test("API Health Check", False, f"Failed to connect to backend: {str(e)}")
            return False
    
    def test_root_endpoint(self):
        """Test root API endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/api/", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if "message" in data and "version" in data:
                    self.log_test("Root Endpoint", True, "Root endpoint working correctly")
                    return True
                else:
                    self.log_test("Root Endpoint", False, "Root endpoint missing expected fields", {"response": data})
                    return False
            else:
                self.log_test("Root Endpoint", False, f"Root endpoint returned status {response.status_code}")
                return False
                
        except requests.exceptions.RequestException as e:
            self.log_test("Root Endpoint", False, f"Failed to connect to root endpoint: {str(e)}")
            return False
    
    def test_portfolio_data(self):
        """Test 2: Portfolio Data - Test GET /api/portfolio endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/api/portfolio", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Validate portfolio structure
                required_fields = ["id", "personal", "projects", "experience", "updated_at"]
                missing_fields = [field for field in required_fields if field not in data]
                
                if missing_fields:
                    self.log_test("Portfolio Data Structure", False, f"Missing required fields: {missing_fields}")
                    return False
                
                # Validate personal info structure
                personal = data.get("personal", {})
                personal_required = ["name", "title", "email", "phone", "location", "linkedin", "github"]
                missing_personal = [field for field in personal_required if field not in personal]
                
                if missing_personal:
                    self.log_test("Portfolio Personal Data", False, f"Missing personal fields: {missing_personal}")
                    return False
                
                # Validate projects structure
                projects = data.get("projects", [])
                if not isinstance(projects, list):
                    self.log_test("Portfolio Projects Data", False, "Projects should be a list")
                    return False
                
                if projects:
                    project = projects[0]
                    project_required = ["id", "title", "description", "image", "github", "technologies", "category"]
                    missing_project = [field for field in project_required if field not in project]
                    
                    if missing_project:
                        self.log_test("Portfolio Projects Structure", False, f"Missing project fields: {missing_project}")
                        return False
                
                # Validate experience structure
                experience = data.get("experience", [])
                if not isinstance(experience, list):
                    self.log_test("Portfolio Experience Data", False, "Experience should be a list")
                    return False
                
                if experience:
                    exp = experience[0]
                    exp_required = ["id", "title", "company", "duration", "description", "technologies"]
                    missing_exp = [field for field in exp_required if field not in exp]
                    
                    if missing_exp:
                        self.log_test("Portfolio Experience Structure", False, f"Missing experience fields: {missing_exp}")
                        return False
                
                self.log_test("Portfolio Data", True, f"Complete portfolio data retrieved with {len(projects)} projects and {len(experience)} experiences")
                return True
                
            else:
                self.log_test("Portfolio Data", False, f"Portfolio endpoint returned status {response.status_code}", {"response": response.text})
                return False
                
        except requests.exceptions.RequestException as e:
            self.log_test("Portfolio Data", False, f"Failed to get portfolio data: {str(e)}")
            return False
    
    def test_personal_info(self):
        """Test 3: Personal Info - Test GET /api/portfolio/personal endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/api/portfolio/personal", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Validate personal info structure
                required_fields = ["name", "title", "email", "phone", "location", "linkedin", "github"]
                missing_fields = [field for field in required_fields if field not in data]
                
                if missing_fields:
                    self.log_test("Personal Info", False, f"Missing required fields: {missing_fields}")
                    return False
                
                # Validate expected data from seed
                expected_name = "Surabhi Santosh Pilane"
                if data.get("name") != expected_name:
                    self.log_test("Personal Info Data", False, f"Expected name '{expected_name}', got '{data.get('name')}'")
                    return False
                
                self.log_test("Personal Info", True, f"Personal info retrieved for {data.get('name')}")
                return True
                
            else:
                self.log_test("Personal Info", False, f"Personal info endpoint returned status {response.status_code}", {"response": response.text})
                return False
                
        except requests.exceptions.RequestException as e:
            self.log_test("Personal Info", False, f"Failed to get personal info: {str(e)}")
            return False
    
    def test_projects_endpoint(self):
        """Test 4: Projects - Test GET /api/portfolio/projects endpoint with and without category filtering"""
        try:
            # Test without category filter
            response = self.session.get(f"{self.base_url}/api/portfolio/projects", timeout=10)
            
            if response.status_code != 200:
                self.log_test("Projects Endpoint", False, f"Projects endpoint returned status {response.status_code}")
                return False
            
            all_projects = response.json()
            
            if not isinstance(all_projects, list):
                self.log_test("Projects Data Type", False, "Projects should return a list")
                return False
            
            if not all_projects:
                self.log_test("Projects Data", False, "No projects found in database")
                return False
            
            # Validate project structure
            project = all_projects[0]
            required_fields = ["id", "title", "description", "image", "github", "technologies", "category"]
            missing_fields = [field for field in required_fields if field not in project]
            
            if missing_fields:
                self.log_test("Projects Structure", False, f"Missing project fields: {missing_fields}")
                return False
            
            self.log_test("Projects All", True, f"Retrieved {len(all_projects)} projects without filter")
            
            # Test with category filter - Data Analytics
            response_filtered = self.session.get(f"{self.base_url}/api/portfolio/projects?category=Data Analytics", timeout=10)
            
            if response_filtered.status_code == 200:
                filtered_projects = response_filtered.json()
                
                if not isinstance(filtered_projects, list):
                    self.log_test("Projects Category Filter", False, "Filtered projects should return a list")
                    return False
                
                # Validate all returned projects have the correct category
                for proj in filtered_projects:
                    if proj.get("category") != "Data Analytics":
                        self.log_test("Projects Category Filter", False, f"Project '{proj.get('title')}' has wrong category: {proj.get('category')}")
                        return False
                
                self.log_test("Projects Category Filter", True, f"Retrieved {len(filtered_projects)} Data Analytics projects")
                
                # Test with Machine Learning category
                response_ml = self.session.get(f"{self.base_url}/api/portfolio/projects?category=Machine Learning", timeout=10)
                
                if response_ml.status_code == 200:
                    ml_projects = response_ml.json()
                    
                    for proj in ml_projects:
                        if proj.get("category") != "Machine Learning":
                            self.log_test("Projects ML Filter", False, f"Project '{proj.get('title')}' has wrong category: {proj.get('category')}")
                            return False
                    
                    self.log_test("Projects ML Filter", True, f"Retrieved {len(ml_projects)} Machine Learning projects")
                    return True
                else:
                    self.log_test("Projects ML Filter", False, f"ML filter returned status {response_ml.status_code}")
                    return False
            else:
                self.log_test("Projects Category Filter", False, f"Category filter returned status {response_filtered.status_code}")
                return False
                
        except requests.exceptions.RequestException as e:
            self.log_test("Projects Endpoint", False, f"Failed to get projects: {str(e)}")
            return False
    
    def test_experience_endpoint(self):
        """Test 5: Experience - Test GET /api/portfolio/experience endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/api/portfolio/experience", timeout=10)
            
            if response.status_code == 200:
                experience_data = response.json()
                
                if not isinstance(experience_data, list):
                    self.log_test("Experience Data Type", False, "Experience should return a list")
                    return False
                
                if not experience_data:
                    self.log_test("Experience Data", False, "No experience found in database")
                    return False
                
                # Validate experience structure
                exp = experience_data[0]
                required_fields = ["id", "title", "company", "duration", "description", "technologies"]
                missing_fields = [field for field in required_fields if field not in exp]
                
                if missing_fields:
                    self.log_test("Experience Structure", False, f"Missing experience fields: {missing_fields}")
                    return False
                
                # Validate expected companies from seed data
                companies = [exp.get("company") for exp in experience_data]
                expected_companies = ["Infosys Springboard", "ONGC"]
                
                for expected_company in expected_companies:
                    if expected_company not in companies:
                        self.log_test("Experience Data Validation", False, f"Expected company '{expected_company}' not found")
                        return False
                
                self.log_test("Experience Endpoint", True, f"Retrieved {len(experience_data)} experience entries")
                return True
                
            else:
                self.log_test("Experience Endpoint", False, f"Experience endpoint returned status {response.status_code}")
                return False
                
        except requests.exceptions.RequestException as e:
            self.log_test("Experience Endpoint", False, f"Failed to get experience: {str(e)}")
            return False
    
    def test_contact_endpoint(self):
        """Test 6: Contact - Test POST /api/portfolio/contact endpoint with sample data"""
        try:
            # Sample contact data
            contact_data = {
                "name": "Sarah Johnson",
                "email": "sarah.johnson@example.com",
                "message": "Hi Surabhi, I'm impressed by your portfolio and would like to discuss potential collaboration opportunities in data analytics projects."
            }
            
            response = self.session.post(
                f"{self.base_url}/api/portfolio/contact",
                json=contact_data,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            
            if response.status_code == 200:
                response_data = response.json()
                
                # Validate response structure
                required_fields = ["id", "name", "email", "message", "created_at", "read"]
                missing_fields = [field for field in required_fields if field not in response_data]
                
                if missing_fields:
                    self.log_test("Contact Response Structure", False, f"Missing response fields: {missing_fields}")
                    return False
                
                # Validate data matches input
                if response_data.get("name") != contact_data["name"]:
                    self.log_test("Contact Data Validation", False, "Response name doesn't match input")
                    return False
                
                if response_data.get("email") != contact_data["email"]:
                    self.log_test("Contact Data Validation", False, "Response email doesn't match input")
                    return False
                
                if response_data.get("message") != contact_data["message"]:
                    self.log_test("Contact Data Validation", False, "Response message doesn't match input")
                    return False
                
                # Validate default values
                if response_data.get("read") != False:
                    self.log_test("Contact Default Values", False, "New message should have read=False")
                    return False
                
                self.log_test("Contact Endpoint", True, f"Contact message created successfully with ID: {response_data.get('id')}")
                
                # Test retrieving contact messages (optional admin endpoint)
                try:
                    get_response = self.session.get(f"{self.base_url}/api/portfolio/contact", timeout=10)
                    if get_response.status_code == 200:
                        messages = get_response.json()
                        if isinstance(messages, list):
                            self.log_test("Contact Messages Retrieval", True, f"Retrieved {len(messages)} contact messages")
                        else:
                            self.log_test("Contact Messages Retrieval", False, "Contact messages should return a list")
                    else:
                        self.log_test("Contact Messages Retrieval", False, f"Get contact messages returned status {get_response.status_code}")
                except:
                    # This is optional, so we don't fail the main test
                    self.log_test("Contact Messages Retrieval", False, "Could not retrieve contact messages (optional feature)")
                
                return True
                
            else:
                self.log_test("Contact Endpoint", False, f"Contact endpoint returned status {response.status_code}", {"response": response.text})
                return False
                
        except requests.exceptions.RequestException as e:
            self.log_test("Contact Endpoint", False, f"Failed to create contact message: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Run all backend API tests"""
        print(f"\n🚀 Starting Portfolio Backend API Tests")
        print(f"Backend URL: {self.base_url}")
        print("=" * 60)
        
        tests = [
            self.test_api_health_check,
            self.test_root_endpoint,
            self.test_portfolio_data,
            self.test_personal_info,
            self.test_projects_endpoint,
            self.test_experience_endpoint,
            self.test_contact_endpoint
        ]
        
        passed = 0
        total = len(tests)
        
        for test in tests:
            try:
                if test():
                    passed += 1
            except Exception as e:
                self.log_test(test.__name__, False, f"Test failed with exception: {str(e)}")
        
        print("\n" + "=" * 60)
        print(f"📊 Test Results: {passed}/{total} tests passed")
        
        if passed == total:
            print("🎉 All tests passed! Backend API is working correctly.")
            return True
        else:
            print(f"⚠️  {total - passed} tests failed. Check the details above.")
            return False
    
    def get_test_summary(self):
        """Get a summary of test results"""
        passed = sum(1 for result in self.test_results if result["success"])
        total = len(self.test_results)
        
        summary = {
            "total_tests": total,
            "passed": passed,
            "failed": total - passed,
            "success_rate": (passed / total * 100) if total > 0 else 0,
            "results": self.test_results
        }
        
        return summary

def main():
    """Main test execution"""
    tester = PortfolioAPITester(BACKEND_URL)
    
    success = tester.run_all_tests()
    
    # Print detailed results
    summary = tester.get_test_summary()
    print(f"\n📈 Success Rate: {summary['success_rate']:.1f}%")
    
    # Return appropriate exit code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()