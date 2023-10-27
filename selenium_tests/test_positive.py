import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPositiveScenarios:
    
    @pytest.mark.positive
    def test_positive(self, driver):
        # Go to webpage
        driver.get("http://127.0.0.1:5173/")
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
        time.sleep(10)

        # Verify if the login was successful by checking the URL
        current_url = driver.current_url
        assert current_url == "http://127.0.0.1:5173/#/home"

        # Secondary verification by checking the text on the page
        # Looks for first role listings
        role_listing_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(., 'Admin Executive')]/following-sibling::div//button[contains(., 'See more')]")))
        role_listing_locator.click()

        # Verifies the new URL after clikcing on the "see more" button
        current_url = driver.current_url
        assert current_url == "http://127.0.0.1:5173/#/role/Admin%20Executive"
        time.sleep(10)

        # Verfies "Edit" and "Apply" button are present
        edit_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Edit')]")))
        apply_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Apply')]")))
        assert edit_button_locator.is_displayed() and apply_button_locator.is_displayed()
