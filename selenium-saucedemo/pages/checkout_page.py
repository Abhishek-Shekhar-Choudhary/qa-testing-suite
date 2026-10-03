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
        for locator, value in (
            (self.FIRST_NAME, first),
            (self.LAST_NAME, last),
            (self.POSTAL, postal),
        ):
            field = self.wait.until(EC.element_to_be_clickable(locator))
            field.send_keys(value)
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE)).click()
        self.wait.until(EC.visibility_of_element_located(self.FINISH))

    def finish_order(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH)).click()
        self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))

    def get_confirmation_header_text(self) -> str:
        self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))
        return self.driver.find_element(*self.COMPLETE_HEADER).text
