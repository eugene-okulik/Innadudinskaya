from playwright.sync_api import Page


def test_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name="Form Authentication").click()

    username_field = page.get_by_role('textbox', name="Username")
    username_field.fill('tomsmith')

    password_field = page.get_by_role('textbox', name='Password')
    password_field.fill('SuperSecretPassword!')

    page.get_by_role('button').click()
