import time

from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure
class ShadowDomPage(BasePage):
    SHADOW_HOST = (By.CSS_SELECTOR, "guid-generator")

    @allure.step("Получение shadow root для элемента")
    def _get_shadow_root(self):
        host = self.find_element(*self.SHADOW_HOST)
        return self.driver.execute_script("return arguments[0].shadowRoot", host)


    @allure.step("Клик на иконку 'fa-cog' для генерации GUID")
    def click_generate(self):
        shadow_root = self._get_shadow_root()
        cog_icon = shadow_root.find_element(By.ID, "buttonGenerate")
        cog_icon.click()
        time.sleep(2)

    @allure.step("Клик на иконку 'fa-clone' для копирования GUID")
    def click_copy(self):
        shadow_root = self._get_shadow_root()
        clone_icon = shadow_root.find_element(By.ID, "buttonCopy")
        clone_icon.click()

    @allure.step("Получение текущего GUID из поля ввода внутри shadow root")
    def get_guid_from_field(self) -> str:
        shadow_root = self._get_shadow_root()
        edit_field = shadow_root.find_element(By.CSS_SELECTOR, "#editField")
        return edit_field.get_attribute("value")
