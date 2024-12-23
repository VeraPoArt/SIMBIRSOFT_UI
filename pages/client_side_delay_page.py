from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time



class ClientSideDelayPage(BasePage):
    BUTTON_LOCATOR = (By.ID, "ajaxButton")
    RESULT_LOCATOR = (By.CSS_SELECTOR, ".bg-success")

    @allure.step("Нажатие на кнопку с локатором")
    def click_button(self):
        self.find_element(*self.BUTTON_LOCATOR).click()

    @allure.step("Ожидание появления success-сообщения до 15 секунд")
    def wait_for_data(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.RESULT_LOCATOR),
            message=f"Сообщение p.bg-success не появилось в течение {timeout} cек"
        )
        return self.find_element(*self.RESULT_LOCATOR).text