import pytest
import time
from datetime import timedelta  # Import timedelta
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from freezegun import freeze_time
# from datetime import datetime
from selenium.common.exceptions import ElementClickInterceptedException


class TestNegativeScenarios:
    
    @pytest.mark.negative
    def test_negative_search(self, driver):
        driver.get("http://localhost:5173/")
        # Declare wait for elements load
        wait = WebDriverWait(driver, 20)

        # Find the input field for the login
        login_locator = driver.find_element(By.ID, "email")
        login_locator.send_keys("Susan Goh")

         # Wait for the autocomplete to appear
        autocomplete_dropdown = wait.until(EC.visibility_of_element_located((By.NAME, "autocomplete")))

        # Locate the desired option
        autocomplete_option = driver.find_element(By.XPATH, "//div[contains(text(), 'dept: Sales')]")
        autocomplete_option.click()

        # Press on the login button
        login_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-primary w-full text-btn') and contains(text(), 'Login')]")))
        login_button_locator.click()
        time.sleep(10)

        # Verify if the login was successful by checking the URL
        current_url = driver.current_url
        assert current_url == "http://localhost:5173/#/home"

        # Secondary verification by checking search box
        search_box_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='form-control rounded' and @placeholder='IT, human resources, finance']")))
        search_box_locator.send_keys("Account Manager")
        
        # Checks for error message
        error_message_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(., 'Oops! No listings found.')]")))
        assert error_message_locator.is_displayed()
    
    @pytest.mark.negative
    def test_negative_editDescription(self, driver):
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
        # Looks for first role listings
        role_listing_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(., 'Consultant')]/following-sibling::div//button[contains(., 'See more')]")))
        driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior = "auto"')
        role_listing_locator.click()

        # Verifies the new URL after clikcing on the "see more" button
        current_url = driver.current_url
        assert current_url == "http://localhost:5173/#/role/Consultant"

        # Verfies "Edit" and "Apply" button are present
        edit_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Edit')]")))
        driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior = "auto"')
        assert edit_button_locator.is_displayed()
        edit_button_locator.click()

        # Switch to the modal element
        driver.switch_to.active_element
        modal_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id='roleDescription']")))
        assert modal_locator.is_displayed()
        # console.log("role_description_locator: ")
        modal_locator.click()
        modal_locator.send_keys(Keys.CONTROL + "a")
        modal_locator.send_keys(Keys.DELETE)
        # modal_locator.clear()

        # After clearing, initiate save changes button
        save_changes_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Save Changes')]")))
        save_changes_button_locator.click()
        
        # Error message locator
        error_message_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(., 'Role description cannot be empty.')]")))
        assert error_message_locator.is_displayed()

    # @pytest.mark.time
    # def test_timeScenario(self, driver):
    #     # Set the current_time to "2024-03-01 23:59:55"
    #     driver.get("http://127.0.0.1:5173/")
    #     # Declare wait for elements load
    #     wait = WebDriverWait(driver, 20)


    #     # Find the input field for the login
    #     login_locator = driver.find_element(By.ID, "email")
    #     login_locator.send_keys("Rithy Sok")

    #     # Wait for the autocomplete to appear
    #     autocomplete_dropdown = wait.until(EC.visibility_of_element_located((By.NAME, "autocomplete")))

    #     # Locate the desired option
    #     autocomplete_option = driver.find_element(By.XPATH, "//div[contains(text(), 'rights: HR')]")
    #     autocomplete_option.click()

    #     # Press on the login button
    #     login_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-primary w-full text-btn') and contains(text(), 'Login')]")))
    #     login_button_locator.click()
    #     time.sleep(5)

    #     # Verify if the login was successful by checking the URL
    #     current_url = driver.current_url
    #     assert current_url == "http://127.0.0.1:5173/#/home"

    #     # Secondary verification by checking the text on the page
    #     # Looks for Call Centre role listings
    #     confirm_role_listing_locator = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(., 'Call Centre')]/following-sibling::div//button[contains(., 'See more')]")))
    #     # Move to the element to ensure it's in the viewport
    #     driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior = "auto"')
    #     confirm_role_listing_locator.click()

    #     # To incremenet the time by 5 seconds -- to make it march 2nd
    #     with freeze_time("2024-03-02 00:00:01"):

    #          # Log the current time after the 'with' block
    #         current_time_after = datetime.now()
    #         print("Current time after freeze_time:", current_time_after)
    #         time.sleep(20)

    #         # Check for Apply button 
    #         driver.switch_to.active_element
    #         # Check for Apply button
    #         apply_button_locator = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-primary text-btn') and contains(text(), 'Apply')]")))

    #         # Handle overlay or other elements that may be intercepting the button
    #         try:
    #             apply_button_locator.click()
    #         except ElementClickInterceptedException:
    #             # If the button click is intercepted, you can wait for the overlay to disappear or for a specific condition to be met
    #             # For example, if it's a modal, you can wait for it to be invisible:
    #             wait.until_not(EC.visibility_of_element_located((By.XPATH, "//div[@id='confirmApplyModal']")))
    #             # Then, try clicking the button again
    #             apply_button_locator.click()

    #         # Waits for the confirmation button to appear
    #         cfm_btn_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(., 'Confirm')]")))
    #         cfm_btn_locator.click()

    #         # Waits for the confirmation message to appear
    #         confirmation_msg_locator = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(., 'Role listing has expired')]")))
    #         assert confirmation_msg_locator.is_displayed()
