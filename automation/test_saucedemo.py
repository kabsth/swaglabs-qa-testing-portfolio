import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

class TestSwagLabs:

    def test_01_valid_login(self, driver):
        """Valid login test"""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert "Products" in driver.title or "Products" in driver.page_source

    def test_02_invalid_login(self, driver):
        """Invalid credentials test"""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("wrong_user")
        driver.find_element(By.ID, "password").send_keys("wrong_pass")
        driver.find_element(By.ID, "login-button").click()
        error_msg = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        assert "Username and password do not match" in error_msg

    def test_03_add_to_cart(self, driver):
        """Add item to cart test"""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_badge == "1"
