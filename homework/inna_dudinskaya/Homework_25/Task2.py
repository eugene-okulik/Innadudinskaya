import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.set_window_size(271, 800)
    yield chrome_driver
    chrome_driver.quit()


def test_practice_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'practice-form-wrapper')))

    # Filling in the form

    # 1. First Name
    driver.find_element(By.ID, 'firstName').send_keys('Inna')

    # 2. Last Name
    driver.find_element(By.ID, "lastName").send_keys('Dudinskaya')

    # 3. Email
    driver.find_element(By.ID, "userEmail").send_keys('inna.dudinskaya@gmail.com')

    # 4. Gender (Female)
    driver.find_element(By.ID, "gender-radio-2").click()

    # 5. Mobile
    driver.find_element(By.ID, "userNumber").send_keys('8297643801')

    # 6. Date of Birth
    date_of_birth_input = driver.find_element(By.ID, "dateOfBirthInput")

    subjects = driver.find_element(By.ID, "subjectsInput")
    actions = ActionChains(driver)
    actions.scroll_to_element(subjects).perform()

    date_of_birth_input.click()

    # Month selecting
    month_select = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".react-datepicker__month-select"))
    )
    month_select.click()

    month_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "option[value='6']"))
    )
    month_option.click()

    # Year selecting
    year_select = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".react-datepicker__year-select"))
    )
    year_select.click()

    year_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "option[value='1984']"))
    )
    year_option.click()

    # Day selecting
    day = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".react-datepicker__day--028"))
    )
    day.click()

    # 7. Subjects
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Computer Science")
    subjects.send_keys(Keys.ENTER)

    # 8. Hobbies
    current_address = driver.find_element(By.ID, "currentAddress")
    actions.scroll_to_element(current_address).perform()
    driver.find_element(By.ID, "hobbies-checkbox-1").click()
    driver.find_element(By.ID, "hobbies-checkbox-2").click()

    # Scroll the page to the bottom
    elem = driver.find_element(By.TAG_NAME, "html")
    elem.send_keys(Keys.END)

    # 9. Address
    driver.find_element(By.ID, "currentAddress").send_keys("Minsk city, Pritytskogo street, 136")

    # 10. State
    state_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "state"))
    )
    state_element.click()

    state_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'NCR')]"))
    )
    state_option.click()

    # 11. City
    city_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "city"))
    )
    city_element.click()

    city_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Delhi')]"))
    )
    city_option.click()

    # 12. Submit
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 13. Result Window
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
    )

    rows = modal.find_element(By.CLASS_NAME, "modal-body").find_elements(By.TAG_NAME, "tr")

    # 14. Results Print
    print("\n" + "=" * 50)
    print("📋 ДАННЫЕ ИЗ ФОРМЫ:")
    print("=" * 50)
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) == 2:
            print(f"{cells[0].text}: {cells[1].text}")
    print("=" * 50)
