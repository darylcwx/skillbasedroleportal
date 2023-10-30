import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestBoundaryScenarios:

    # HR view empty listings in Home Page (IS212-G2-listings-002)
    @pytest.mark.boundary
    def test_boundary_empty_data(self, driver):
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
        time.sleep(5)

        # Verify if the login was successful by checking the URL
        current_url = driver.current_url
        assert current_url == "http://127.0.0.1:5173/#/home"

        # Looks for the "Internal server error message as designed"
        error_message_Locator = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='flex flex-col']//div[text()=' Oops! Internal Server Error occurred. ']")))
        assert error_message_Locator.is_displayed()
        assert "Oops! Internal Server Error occurred." in error_message_Locator.text