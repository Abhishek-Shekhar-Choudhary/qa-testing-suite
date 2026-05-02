from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    TITLE = (By.CSS_SELECTOR, '[data-test="title"]')
    ADD_BACKPACK = (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
    CART_LINK = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')

    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.TITLE))

    def add_backpack_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BACKPACK)).click()

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
