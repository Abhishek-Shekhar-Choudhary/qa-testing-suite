from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_when_user_adds_backpack_cart_page_opens_with_expected_url(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.wait_loaded()
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    cart = CartPage(driver)
    cart.wait_loaded()
    assert "cart" in driver.current_url, "expected SauceDemo cart route after opening cart"


def test_when_user_completes_checkout_order_confirmation_is_shown(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.wait_loaded()
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    cart = CartPage(driver)
    cart.wait_loaded()
    cart.start_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_shipping_and_continue("Alex", "QA", "94105")
    checkout.finish_order()

    header = checkout.get_confirmation_header_text()
    assert "Thank you" in header, f"expected thank-you header, got: {header!r}"
