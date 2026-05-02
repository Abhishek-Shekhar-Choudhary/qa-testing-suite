import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,720")

    service = ChromeService(ChromeDriverManager().install())
    wd = webdriver.Chrome(service=service, options=options)
    wd.implicitly_wait(0)

    yield wd

    wd.quit()
