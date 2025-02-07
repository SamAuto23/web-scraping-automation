from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# LinkedIn login credentials
USERNAME = "your_email@example.com"
PASSWORD = "yourpassword"

# LinkedIn job search URL (modify filters as needed)
JOB_SEARCH_URL = "https://www.linkedin.com/jobs/search/?keywords=software%20engineer"

def linkedin_auto_apply():
    # Set up Selenium Chrome driver
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")

    # Log in
    driver.find_element("id", "username").send_keys(USERNAME)
    driver.find_element("id", "password").send_keys(PASSWORD)
    driver.find_element("xpath", "//button[@type='submit']").click()

    time.sleep(3)  # Wait for page to load

    # Go to job search page
    driver.get(JOB_SEARCH_URL)
    time.sleep(3)

    # Apply to jobs (simplified version)
    jobs = driver.find_elements("xpath", "//button[contains(@class, 'jobs-apply-button')]")
    
    for job in jobs[:3]:  # Apply to the first 3 jobs
        job.click()
        time.sleep(2)
        try:
            apply_button = driver.find_element("xpath", "//button[contains(text(), 'Easy Apply')]")
            apply_button.click()
            time.sleep(2)
        except:
            print("❌ No Easy Apply option available for this job.")

    driver.quit()
    print("✅ Applied to available jobs.")

linkedin_auto_apply()

