import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_hover_and_add_to_cart_simple(driver):
    driver.get('http://testshop.qa-practice.com/')
    wait = WebDriverWait(driver, 10)

    product_image = wait.until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='Customizable Desk']"))
    )
    product_title = product_image.get_attribute("alt")
    print(f"\n Product: '{product_title}'")

    ActionChains(driver).move_to_element(product_image).perform()

    add_to_cart_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-primary a-submit']"))
    )
    add_to_cart_btn.click()

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-body")))

    popup_product = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, f"//strong[contains(text(), '{product_title}')]"))
    )
    assert popup_product.is_displayed()
    print(f" Product '{product_title}' is in pop-up!")
