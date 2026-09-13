import pytest
from test_UI_innadudinskaya_pw.pages.cart_page import CartPage
from test_UI_innadudinskaya_pw.pages.category_page import CategoryPage
from test_UI_innadudinskaya_pw.pages.product_page import ProductPage


@pytest.fixture()
def cart_page(page):
    return CartPage(page)


@pytest.fixture()
def category_page(page):
    return CategoryPage(page)


@pytest.fixture()
def product_page(page):
    return ProductPage(page)


@pytest.fixture()
def cart_with_product(page, category_page, product_page):
    category_page.open_page()
    category_page.open_product(2)
    product_page.add_to_cart()
    product_page.wait_good_added_to_cart()
    cart_page = CartPage(page)
    cart_page.open_page()
    return cart_page
