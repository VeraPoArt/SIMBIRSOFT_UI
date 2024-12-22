import pytest
from pages import LoginPage, InventoryPage
import allure
@allure.testcase("TMS-002", "Авторизация с пустым полем пароля")
@allure.title("Авторизация с пустым полем пароля")
@allure.severity(allure.severity_level.CRITICAL)
def test_empty_password(driver):
    login_page = LoginPage(driver)
    initial_url = login_page.get_current_url()
    login_page.input_login('standard_user')
    login_page.login_button_click()
    assert login_page.get_current_url() == initial_url
    assert login_page.get_error_message() == "Epic sadface: Password is required"

@allure.title("Авторизация с пустым полем пароля и логина")
@allure.testcase("TMS-001", "Авторизация с пустым полем пароля и логина")
@allure.severity(allure.severity_level.MINOR)
def test_auth_failed(driver):
    login_page = LoginPage(driver)
    login_page.input_login('')
    assert login_page.get_attribute(login_page.login, "value") == "", "Поле логина не пустое"
    login_page.input_password('')
    assert login_page.get_attribute(login_page.password, "value") == "", "Поле пароля не пустое"
    login_page.login_button_click()
    assert login_page.check_login_page_open(), "Произошёл переход с текущей страницы"
    assert login_page.get_error_message() == "Epic sadface: Password is required", \
        "Сообщение об ошибке не соответствует ожидаемому"

@allure.testcase("TMS-003", "Авторизация с некорректным паролем")
@allure.title("Авторизация с некорректным паролем")
@allure.severity(allure.severity_level.NORMAL)
def test_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.input_login('standard_user')
    login_page.input_password('wrong_password')
    login_page.login_button_click()
    assert login_page.check_login_page_open()
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"



@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
])
@allure.testcase("TMS-004", "Авторизация с валидными данными")
@allure.title("Авторизация с валидными данными")
@allure.severity(allure.severity_level.CRITICAL)
def test_auth(driver, username, password):
    auth_page = LoginPage(driver)
    auth_page.input_login(username)
    auth_page.input_password(password)
    auth_page.login_button_click()
    assert InventoryPage(driver).check_inventory_page_open()