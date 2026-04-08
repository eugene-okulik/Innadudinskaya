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


def test_single_select(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')

    select_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "id_choose_language"))
    )
    select_element.click()

    python_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "option[value='1']"))
    )
    python_option.click()

    driver.find_element(By.ID, "submit-id-submit").click()

    result_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'result-text'))
    )

    print(f"\n Chosen language: '{result_text.text}'")
    assert result_text.text == "Python"
