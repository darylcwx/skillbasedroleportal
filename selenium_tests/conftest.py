import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    try: 
        print("Creating chrome driver")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        yield my_driver
        print("Closing chrome driver")
        my_driver.quit()
    except Exception as e:
        print(e)
    
