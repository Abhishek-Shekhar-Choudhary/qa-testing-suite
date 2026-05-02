from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    CHECKOUT = (By.CSS_SELECTOR, '[data-test="checkout"]')
    CART_ITEM = (By.CSS_SELECTOR, '[data-test="cart-list"]')

    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_ITEM))

    def start_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT)).click()
