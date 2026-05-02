from pages.login_page import LoginPage


def test_when_credentials_are_valid_user_reaches_inventory(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url, "expected SauceDemo inventory URL after successful login"


def test_when_password_is_invalid_error_is_shown_and_inventory_is_not_opened(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "not_secret_sauce")
    assert login.is_error_visible(), "expected login error banner for invalid password"
    assert "inventory" not in driver.current_url, "expected to remain off inventory when login fails"
