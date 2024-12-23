import allure
import pytest
from pages.client_side_delay_page import ClientSideDelayPage



@allure.testcase("TMS-012", "Client Side Delay")
@allure.title("Проверка задержки на клиенте")
@allure.severity(allure.severity_level.NORMAL)
def test_client_side_delay(driver, base_url):
    page = ClientSideDelayPage(driver)
    page.open(f"{base_url}/clientdelay")
    page.click_button()
    result = page.wait_for_data(timeout=15)
    assert "Data calculated on the client side." in result, "Не получены данные или текст неверен"
