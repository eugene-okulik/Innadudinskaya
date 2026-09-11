def test_cart_page_main_elements(cart_with_product):
    cart_with_product.check_url_contains('cart')
    cart_with_product.check_title_contains('Cart')
    cart_with_product.check_order_overview_exists()
    cart_with_product.check_checkout_button_exists()
    cart_with_product.check_continue_shopping_link_exists()
    cart_with_product.check_remove_button_exists()


def test_continue_shopping_link(cart_with_product):
    cart_with_product.click_continue_shopping()
    cart_with_product.check_url_contains('/shop')


def test_remove_product_from_cart(cart_with_product):
    cart_with_product.remove_product()
    assert cart_with_product.is_cart_empty(), "Empty cart message is not displayed"


def test_proceed_to_checkout(cart_with_product):
    cart_with_product.proceed_to_checkout()
    cart_with_product.check_url_contains('address')
