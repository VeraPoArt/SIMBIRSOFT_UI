import allure
import pytest
from pages.ajax_data_page import AjaxDataPage

@allure.testcase("TMS-011", "AjaxData")
@allure.title("Проверка задержки AJAX-запроса к веб-серверу")
@allure.severity(allure.severity_level.NORMAL)
def test_ajax_data(driver, base_url):
    page = AjaxDataPage(driver)
    page.open(f"{base_url}/ajax")
    page.trigger_ajax()
    result = page.wait_for_data(timeout=15)
    assert "Data loaded with AJAX get request." in result, "Не получены данные или текст неверен"

