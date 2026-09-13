from test_UI_innadudinskaya_pw.pages.base_page import BasePage
from test_UI_innadudinskaya_pw.pages.locators import product_page_locators as loc
from playwright.sync_api import expect


class ProductPage(BasePage):

    def __init__(self, page, product_id='furn-9999-office-design-software-7', category='9'):
        super().__init__(page)
        self.page_url = f'/shop/{product_id}?category={category}'

    def check_success_message(self):
        self.check_element_text("Item(s) added to your cart", loc.success_message_loc)

    def check_product_title_is_not_empty(self):
        title = self.find(loc.product_title_loc)
        expect(title).not_to_be_empty()

    def check_price_is_displayed(self):
        self.check_element_displayed(loc.product_price_loc)

    def check_product_image_exists(self):
        self.check_element_displayed(loc.product_image_loc)

    def check_add_to_cart_button_exists(self):
        self.check_element_displayed(loc.add_to_cart_button_loc)

    def add_to_cart(self):
        self.click(loc.add_to_cart_button_loc)

    def wait_good_added_to_cart(self):
        self.check_element_displayed(loc.cart_item_added_loc)

    def check_quantity_input_exists(self):
        self.check_element_displayed(loc.quantity_input_loc)

    def check_plus_button_exists(self):
        self.check_element_displayed(loc.plus_button_loc)

    def check_minus_button_exists(self):
        self.check_element_displayed(loc.minus_button_loc)

    def get_current_quantity(self) -> int:
        qty_input = self.find(loc.quantity_input_loc)
        return int(qty_input.input_value())

    def click_plus(self):
        current = self.get_current_quantity()
        self.click(loc.plus_button_loc)
        self.page.wait_for_function(
            f"document.querySelector(\"input[name='add_qty']\").value !== '{current}'"
        )

    def click_minus(self):
        current = self.get_current_quantity()
        self.click(loc.minus_button_loc)
        self.page.wait_for_function(
            f"document.querySelector(\"input[name='add_qty']\").value !== '{current}'"
        )
