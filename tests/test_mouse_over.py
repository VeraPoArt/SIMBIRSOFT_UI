import allure
import pytest
from pages.mouse_over_page import MouseOverPage



@allure.testcase("TMS-013", "Mouse Over")
@allure.title("Проверка кликов по ссылкам Click me и Link Button")
@allure.severity(allure.severity_level.NORMAL)
def test_mouse_over(driver, base_url):
    page = MouseOverPage(driver)
    page.open(f"{base_url}/mouseover")


    initial_click_me = page.get_click_me_count()
    for _ in range(10):
        page.hover_and_click_click_me()
    new_click_me = page.get_click_me_count()
    assert new_click_me == initial_click_me + 10, (
        f"Счётчик Click me не увеличился на 2: было {initial_click_me}, стало {new_click_me}"
    )


    initial_link_button = page.get_link_button_count()
    for _ in range(15):
        page.hover_and_click_link_button()
    new_link_button = page.get_link_button_count()
    assert new_link_button == initial_link_button + 15, (
        f"Счётчик Link Button не увеличился на 2: было {initial_link_button}, стало {new_link_button}"
    )
