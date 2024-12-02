from pages import LoginPage

def test_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.input_login('standard_user')
    login_page.input_password('wrong_password')
    login_page.login_button_click()
    assert login_page.check_login_page_open()
    expected_error = "Epic sadface: Username and password do not match any user in this service"
    assert login_page.get_error_message() == expected_error