from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    USERNAME = (By.CSS_SELECTOR, '[data-test="username"]')
    PASSWORD = (By.CSS_SELECTOR, '[data-test="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')
    ERROR_BOX = (By.CSS_SELECTOR, '[data-test="error"]')

    def __init__(self, driver, base_url: str = "https://www.saucedemo.com/", timeout: int = 15):
        self.driver = driver
        self.base_url = base_url.rstrip("/") + "/"
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.base_url)

    def login(self, username: str, password: str):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_error_visible(self) -> bool:
        self.wait.until(EC.visibility_of_element_located(self.ERROR_BOX))
        return self.driver.find_element(*self.ERROR_BOX).is_displayed()
