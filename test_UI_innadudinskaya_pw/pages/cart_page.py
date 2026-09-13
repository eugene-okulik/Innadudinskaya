from playwright.sync_api import Error as PlaywrightError
from test_UI_innadudinskaya_pw.pages.base_page import BasePage
from test_UI_innadudinskaya_pw.pages.locators import cart_page_locators as loc


class CartPage(BasePage):
    page_url = '/shop/cart'

    def check_checkout_button_exists(self):
        self.check_element_displayed(loc.checkout_button_loc)

    def check_order_overview_exists(self):
        self.check_element_text("Order overview", loc.order_overview_loc)

    def check_continue_shopping_link_exists(self):
        self.check_element_displayed(loc.continue_shopping_link_loc)

    def check_remove_button_exists(self):
        self.check_element_displayed(loc.remove_button_loc)

    def proceed_to_checkout(self):
        self.click(loc.checkout_button_loc)

    def remove_product(self):
        self.click(loc.remove_button_loc)

    def click_continue_shopping(self):
        self.click(loc.continue_shopping_link_loc)

    def is_cart_empty(self) -> bool:
        return self.is_element_visible(loc.empty_cart_message_loc)

    def is_element_visible(self, locator: str) -> bool:
        try:
            element = self.find(locator)
            return element.is_visible()
        except PlaywrightError:
            return False
