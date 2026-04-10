import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_id_selector(driver):
    input_data = 'cat'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'id_text_string')))
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'result-text')))
    print(f"\n Result text: '{result_text.text}'")
    assert result_text.text == input_data
