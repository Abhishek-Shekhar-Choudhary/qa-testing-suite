from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    FIRST_NAME = (By.CSS_SELECTOR, '[data-test="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, '[data-test="lastName"]')
    POSTAL = (By.CSS_SELECTOR, '[data-test="postalCode"]')
    CONTINUE = (By.CSS_SELECTOR, '[data-test="continue"]')
    FINISH = (By.CSS_SELECTOR, '[data-test="finish"]')
    COMPLETE_HEADER = (By.CSS_SELECTOR, '[data-test="complete-header"]')

    def __init__(self, driver, timeout: int = 25):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def fill_shipping_and_continue(self, first: str, last: str, postal: str):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.POSTAL).send_keys(postal)
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE)).click()
        self.wait.until(EC.url_contains("checkout-step-two"))

    def finish_order(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH)).click()
        self.wait.until(EC.url_contains("checkout-complete"))

    def get_confirmation_header_text(self) -> str:
        self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))
        return self.driver.find_element(*self.COMPLETE_HEADER).text
