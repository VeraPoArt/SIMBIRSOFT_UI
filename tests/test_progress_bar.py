import allure
import pytest
from pages.progress_bar_page import ProgressBarPage



@allure.testcase("TMS-014", "Progress Bar")
@allure.title("Проверка прогресс бара до 75% и остановка")
@allure.severity(allure.severity_level.CRITICAL)
def test_progress_bar(driver, base_url):
    page = ProgressBarPage(driver)
    page.open(f"{base_url}/progressbar")

    page.click_start()
    val = page.wait_for_value_reach(target=75, timeout=20)
    page.click_stop()
    final_val = page.get_progress_value()

    diff = abs(final_val - 75)
    assert diff <= 10, (
        f"Значение прогресс бара слишком далеко от 75: {final_val}, разница: {diff}"
    )
