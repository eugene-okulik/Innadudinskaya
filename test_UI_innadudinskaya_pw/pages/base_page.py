from playwright.sync_api import Page, expect
import re


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator: str):
        return self.page.locator(locator).first

    def find_all(self, locator: str):
        return self.page.locator(locator).all()

    def click(self, locator: str):
        self.page.locator(locator).first.click()

    def check_url_contains(self, text: str):
        pattern = re.compile(f'.*{re.escape(text)}.*')
        expect(self.page).to_have_url(pattern)

    def check_title_contains(self, text: str):
        pattern = re.compile(re.escape(text), re.IGNORECASE)
        expect(self.page).to_have_title(pattern)

    def check_element_displayed(self, locator: str):
        element = self.page.locator(locator).first
        expect(element).to_be_visible()

    def check_element_text(self, expected_text: str, locator: str):
        element = self.page.locator(locator).first
        expect(element).to_have_text(expected_text)
