from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открытие страницы")
    def open(self, url: str):
        self.driver.get(url)

    @allure.step("Поиск элемента с локатором")
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    @allure.step("Поиск множества элементов с локатором")
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    @allure.step("Ожидание видимости элемента с локатором")
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
