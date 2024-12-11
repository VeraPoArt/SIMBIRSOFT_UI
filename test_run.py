from pages import LoginPage
import allure


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
