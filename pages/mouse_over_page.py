from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from .base_page import BasePage

class MouseOverPage(BasePage):
    CLICK_ME_LINK = (By.LINK_TEXT, "Click me")
    CLICK_ME_COUNT = (By.CSS_SELECTOR, "#clickCount")

    LINK_BUTTON_LINK = (By.LINK_TEXT, "Link Button")
    LINK_BUTTON_COUNT = (By.CSS_SELECTOR, "#clickButtonCount")

    @allure.step("Наведение мыши на ссылку 'Click me' и клик по ней")
    def hover_and_click_click_me(self):
        """Наводим мышь на ссылку 'Click me' => DOM меняется => заново ищем ссылку => кликаем."""
        link = self.find_element(*self.CLICK_ME_LINK)
        ActionChains(self.driver).move_to_element(link).perform()
        link = self.find_element(*self.CLICK_ME_LINK)
        link.click()

    @allure.step("Получение количества кликов по ссылке 'Click me'")
    def get_click_me_count(self):
        text = self.find_element(*self.CLICK_ME_COUNT).text
        return int(text)

    @allure.step("Наведение мыши на ссылку 'Link Button' и клик по ней")
    def hover_and_click_link_button(self):
        """То же самое, но для «Link Button»."""
        link = self.find_element(*self.LINK_BUTTON_LINK)
        ActionChains(self.driver).move_to_element(link).perform()
        link = self.find_element(*self.LINK_BUTTON_LINK)
        link.click()

    @allure.step("Получение количества кликов по ссылке 'Link Button'")
    def get_link_button_count(self):
        text = self.find_element(*self.LINK_BUTTON_COUNT).text
        return int(text)
