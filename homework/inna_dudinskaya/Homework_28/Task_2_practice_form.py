from playwright.sync_api import Page


def test_practice_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.set_viewport_size({"width": 1280, "height": 800})

    # Filling in the form

    # 1. First Name

    page.get_by_placeholder('First Name').fill('Inna')

    # 2. Last Name

    page.get_by_placeholder('Last Name').fill('Dudinskaya')

    # 3. Email

    page.get_by_placeholder('name@example.com').fill('inna.dudinskaya@gmail.com')

    # 4. Gender (Female)

    page.get_by_label('Female').click()

    # 5. Mobile

    page.get_by_placeholder('Mobile Number').fill('8297643801')

    # 6. Date of Birth

    page.locator('#dateOfBirthInput').click()

    # Month selecting

    page.locator('.react-datepicker__month-select').select_option('6')

    # Year selecting

    page.locator('.react-datepicker__year-select').select_option('1984')

    # Day selecting

    page.locator('.react-datepicker__day--028').click()

    # 7. Subjects

    page.locator('#subjectsInput').fill('Computer Science')
    page.wait_for_selector('.subjects-auto-complete__option', state='visible', timeout=10000)
    page.locator('.subjects-auto-complete__option', has_text='Computer Science').click()

    # 8. Hobbies

    page.get_by_text('Sports').click()
    page.get_by_text('Reading').click()

    # 9. Address

    page.get_by_placeholder('Current Address').fill('Minsk city, Pritytskogo street, 136')

    # 10. State

    page.locator('#state').click()
    page.get_by_text('NCR', exact=True).click()

    # 11. City

    page.locator('#city').click()
    page.get_by_text('Delhi', exact=True).click()

    # 12. Submit
    page.get_by_role('button', name="Submit").click()
