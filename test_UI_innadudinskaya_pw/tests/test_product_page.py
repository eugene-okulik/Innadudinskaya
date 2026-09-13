def test_product_page_main_elements(product_page):
    product_page.open_page()
    product_page.check_url_contains('furn-9999')
    product_page.check_product_title_is_not_empty()
    product_page.check_price_is_displayed()
    product_page.check_product_image_exists()
    product_page.check_add_to_cart_button_exists()
    product_page.check_quantity_input_exists()
    product_page.check_plus_button_exists()
    product_page.check_minus_button_exists()


def test_add_product_to_cart(product_page):
    product_page.open_page()
    product_page.add_to_cart()
    product_page.check_success_message()


def test_increase_decrease_quantity(product_page):
    product_page.open_page()

    initial_value = product_page.get_current_quantity()

    product_page.click_plus()
    assert product_page.get_current_quantity() == initial_value + 1, \
        f"Quantity did not increase: was {initial_value}, now {product_page.get_current_quantity()}"

    product_page.click_minus()
    assert product_page.get_current_quantity() == initial_value, \
        f"Quantity did not decrease back: was {initial_value}, now {product_page.get_current_quantity()}"
