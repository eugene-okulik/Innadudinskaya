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


def test_customizable_desk(driver):
    driver.get('http://testshop.qa-practice.com/')
    wait = WebDriverWait(driver, 10)

    main_tab = driver.current_window_handle

    desk_link = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@content='Customizable Desk']"))
    )

    desk_link.send_keys(Keys.CONTROL + Keys.RETURN)

    wait.until(lambda d: len(d.window_handles) > 1)

    product_tab = None

    for tab in driver.window_handles:
        if tab != main_tab:
            product_tab = tab
            break

    driver.switch_to.window(product_tab)

    add_to_cart_button = wait.until(
        EC.element_to_be_clickable((By.ID, "add_to_cart"))
    )
    add_to_cart_button.click()

    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'btn-secondary')]"))
    )
    continue_button.click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//sup[contains(text(), '1')]")))

    driver.close()

    driver.switch_to.window(main_tab)

    cart_button = driver.find_element(By.CLASS_NAME, "o_navlink_background_hover")
    driver.execute_script("arguments[0].click();", cart_button)

    cart_item = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//a[.//h6[contains(text(), 'Customizable Desk')]]"))
    )

    assert cart_item.is_displayed()
    print("\n'Customizable Desk' item is successfully added to the cart")
