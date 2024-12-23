import allure
import pytest
import time
from pages.shadow_dom_page import ShadowDomPage



@allure.testcase("TMS-015", "Shadow DOM")
@allure.title("Проверка генерации и вставки GUID в поле")
@allure.severity(allure.severity_level.BLOCKER)
def test_shadow_dom(driver, base_url):
    page = ShadowDomPage(driver)
    page.open(f"{base_url}/shadowdom")

    # 1) Генерируем GUID
    page.click_generate()
    guid_before_copy = page.get_guid_from_field()
    assert guid_before_copy, "GUID не сгенерировался!"

    # 2) Нажимаем иконку копирования (которая, допустим, вставляет GUID обратно в поле)
    page.click_copy()
    guid_after_copy = page.get_guid_from_field()
    assert guid_after_copy, "После копирования в поле ничего не оказалось"

    # 3) Проверяем, что значение совпадает
    assert guid_before_copy == guid_after_copy, (
        f"До копирования было {guid_before_copy}, а после копирования стало {guid_after_copy}"
    )
