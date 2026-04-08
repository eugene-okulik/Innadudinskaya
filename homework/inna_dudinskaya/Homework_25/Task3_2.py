import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_dynamic_loading(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']"))
    )
    start_button.click()

    result_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4"))
    )

    print(f"\n result text: '{result_text.text}'")
    assert result_text.text == "Hello World!"
