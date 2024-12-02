from pages import LoginPage

def test_empty_password(driver):
    login_page = LoginPage(driver)
    initial_url = login_page.get_current_url()
    login_page.input_login('standard_user')
    login_page.login_button_click()
    assert login_page.get_current_url() == initial_url
    expected_error = "Epic sadface: Password is required"
    assert login_page.get_error_message() == expected_error