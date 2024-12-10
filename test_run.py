from pages import LoginPage, InventoryPage


def test_auth(driver):
    auth_page = LoginPage(driver)
    auth_page.input_login('')
    assert auth_page.get_attribute(auth_page.login, "value") == "", "Поле логина не пустое"
    auth_page.input_password('')
    assert auth_page.get_attribute(auth_page.password, "value") == "", "Поле пароля не пустое"
    auth_page.login_button_click()
    assert auth_page.check_login_page_open()
    assert auth_page.get_error_message() == "Epic sadface: Password is required"
