from test_UI_innadudinskaya_pw.pages.base_page import BasePage
from test_UI_innadudinskaya_pw.pages.locators import category_page_locators as loc


class CategoryPage(BasePage):

    def __init__(self, page, category='desks-1'):
        super().__init__(page)
        self.page_url = f'/shop/category/{category}'

    def check_url_contains_category(self, category: str):
        self.check_url_contains(category)

    def check_products_exist(self):
        products = self.find_all(loc.product_items_loc)
        assert len(products) > 0, "Products are not found"

    def check_price_slider_exists(self):
        self.check_element_displayed(loc.price_slider_wrapper_loc)

    def check_legs_checkbox_exists(self):
        self.check_element_displayed(loc.first_legs_checkbox_loc)

    def check_categories_dropdown_exists(self):
        self.check_element_displayed(loc.categories_dropdown_loc)

    def open_product(self, product_number: int) -> bool:
        products = self.find_all(loc.product_items_loc)
        if products and len(products) > product_number:
            products[product_number].click()
            return True
        return False

    def get_cart_icon_click(self, cart_icon_number: int):
        cart_icons = self.find_all(loc.items_cart_icons)
        if cart_icons and len(cart_icons) > cart_icon_number:
            cart_icons[cart_icon_number].click()

    def is_add_to_cart_dialog_opened(self):
        self.check_element_displayed(loc.add_to_card_dialog_title)

    def check_sort_dropdown_exists(self):
        self.check_element_displayed(loc.sort_dropdown_loc)

    def open_sort_dropdown(self):
        self.click(loc.sort_dropdown_loc)

    def select_sort_by_price_low_to_high(self):
        self.click(loc.sort_by_price_low_loc)
        self.page.wait_for_url("**order=list_price+asc**", timeout=10000)

    def get_product_prices(self) -> list[float]:
        price_elements = self.page.locator(loc.product_prices_loc).all()
        prices = []
        for el in price_elements:
            text = el.inner_text().replace(",", "").strip()
            if text:
                prices.append(float(text))
        return prices
