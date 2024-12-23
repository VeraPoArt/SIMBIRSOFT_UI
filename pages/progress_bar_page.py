import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class ProgressBarPage(BasePage):
    START_BUTTON = (By.ID, "startButton")
    STOP_BUTTON = (By.ID, "stopButton")
    PROGRESS_BAR = (By.ID, "progressBar")

    @allure.step("Клик по кнопке 'Start' для начала прогресс-бара")
    def click_start(self):
        self.find_element(*self.START_BUTTON).click()

    @allure.step("Клик по кнопке 'Stop' для остановки прогресс-бара")
    def click_stop(self):
        self.find_element(*self.STOP_BUTTON).click()

    @allure.step("Получение текущего значения прогресс-бара")
    def get_progress_value(self) -> int:
        element = self.find_element(*self.PROGRESS_BAR)
        return int(element.get_attribute("aria-valuenow"))

    @allure.step("Ожидание, пока значение прогресс-бара не достигнет 75")
    def wait_for_value_reach(self, target=75, timeout=10) -> int:
        end_time = time.time() + timeout
        while time.time() < end_time:
            value = self.get_progress_value()
            if value >= target:
                return value
            time.sleep(0.1)
        return self.get_progress_value()
