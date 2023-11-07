import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPositiveScenarios:
    
    # View Navigation Options (IS212-G2-NAV-001)
    @pytest.mark.positive
    
    def test_positive_hr_view_navigation(self, driver):
        # Go to webpage
        driver.get("http://localhost:5173/")
        # Declare wait for elements load
        wait = WebDriverWait(driver, 20)
        
        # Find the input field for the login
        login_locator = driver.find_element(By.ID, "email")
        login_locator.send_keys("Rithy Sok")

        # Wait for the autocomplete to appear
        autocomplete_dropdown = wait.until(EC.visibility_of_element_located((By.NAME, "autocomplete")))

        # Locate the desired option
        autocomplete_option = driver.find_element(By.XPATH, "//div[contains(text(), 'rights: HR')]")
        autocomplete_option.click()

        # Press on the login button
        login_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-primary w-full text-btn') and contains(text(), 'Login')]")))
        login_button_locator.click()
        time.sleep(5)

        # Verify if the login was successful by checking the URL
        current_url = driver.current_url
        assert current_url == "http://localhost:5173/#/home"

        # Secondary verification by checking the text on the page
        # Looks for later expired listing for testing - to ensure that all testcases are still up and running
        role_listing_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(., 'Consultant')]/following-sibling::div//button[contains(., 'See more')]")))
        driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior = "auto"')
        role_listing_locator.click()
        time.sleep(3)

        # Verifies the new URL after clikcing on the "see more" button
        current_url = driver.current_url
        assert current_url == "http://localhost:5173/#/role/Consultant"

        # Verfies "Edit" and "Apply" button are present
        edit_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Edit')]")))
        apply_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Apply')]")))
        assert edit_button_locator.is_displayed() and apply_button_locator.is_displayed()

    # View Navigation Options (IS212-G2-NAV-002)
    @pytest.mark.positive
    def test_positive_user_view_navigation(self, driver):
        # Go to webpage
        driver.get("http://localhost:5173/")
        # Declare wait for elements load
        wait = WebDriverWait(driver, 20)

        # Find the input field for the login
        login_locator = driver.find_element(By.ID, "email")
        login_locator.send_keys("Susan Goh")

        # Wait for the autocomplete to appear
        autocomplete_dropdown = wait.until(EC.visibility_of_element_located((By.NAME, "autocomplete")))

        # Locate the desired option
        # Under here we have two susan goh but both belongs to the same user group (user) so its fine to just select any one of them
        autocomplete_option = driver.find_element(By.XPATH, "//div[contains(text(), 'rights: user')]")
        autocomplete_option.click()

         # Press on the login button
        login_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-primary w-full text-btn') and contains(text(), 'Login')]")))
        login_button_locator.click()
        time.sleep(3)

         # Verify if the login was successful by checking the URL
        current_url = driver.current_url
        assert current_url == "http://localhost:5173/#/home"

        # Looks for first role listing provided -- in this case is the developer role listing. 
        role_listing_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(., 'Consultant')]/following-sibling::div//button[contains(., 'See more')]")))
        driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior = "auto"')
        role_listing_locator.click()
        time.sleep(3)

        # Verifies the new URL after clicking on the "see more" button
        current_url = driver.current_url
        assert current_url == "http://localhost:5173/#/role/Consultant"
        
        # Verfies "Apply" button is present
        apply_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Apply')]")))
        assert apply_button_locator.is_displayed()

    # User views compatibility of role (IS212-G2-roleSkillsMatch-001)
    @pytest.mark.positive
    def test_positive_user_view_compatibility(self, driver):
        # Go to webpage
        driver.get("http://localhost:5173/")
        # Declare wait for elements load
        wait = WebDriverWait(driver, 20)

        # Find the input field for the login
        login_locator = driver.find_element(By.ID, "email")
        login_locator.send_keys("Jack Goh")

        # Wait for the autocomplete to appear
        autocomplete_dropdown = wait.until(EC.visibility_of_element_located((By.NAME, "autocomplete")))

        # Locate the desired option
        # Under here we have two susan goh but both belongs to the same user group (user) so its fine to just select any one of them
        autocomplete_option = driver.find_element(By.XPATH, "//div[contains(text(), 'rights: HR')]")
        autocomplete_option.click()

         # Press on the login button
        login_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-primary w-full text-btn') and contains(text(), 'Login')]")))
        login_button_locator.click()
        time.sleep(3)

         # Verify if the login was successful by checking the URL
        current_url = driver.current_url
        assert current_url == "http://localhost:5173/#/home"

        # Look for a role listing that is provided
        role_listing_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(., 'Consultant')]/following-sibling::div//button[contains(., 'See more')]")))
        driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior = "auto"')
        role_listing_locator.click()
        time.sleep(3)

        # Verfies the URL after clicking on the "see more" button
        current_url = driver.current_url
        assert current_url == "http://localhost:5173/#/role/Consultant"

        # Finds the modal first before proceeding
        skills_required_modal = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'custom-modal')]//div[contains(text(), 'Skills Required')]")))
        assert skills_required_modal.is_displayed()
        
        # Finds the matched skills and mismatched skills
        matched_skills_locator = skills_required_modal.find_elements(By.XPATH, "//div[@name='matched']//span[contains(@class, 'badge custom-pill bg-success')]")
        assert len(matched_skills_locator) > 0
        mismatched_skills_locator = skills_required_modal.find_elements(By.XPATH, "//div[@name='matched']//span[contains(@class, 'badge custom-pill bg-secondary')]")
        assert len(mismatched_skills_locator) > 0

        # Verifies percentage
        percentage_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'My percentage match:') and .//b[text()!='0.00%']]")))
        assert percentage_locator.is_displayed()