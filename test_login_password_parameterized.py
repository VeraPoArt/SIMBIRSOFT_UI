import pytest
from pages import LoginPage, InventoryPage

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
])

def test_auth(driver, username, password):
    auth_page = LoginPage(driver)
    auth_page.input_login(username)
    auth_page.input_password(password)
    auth_page.login_button_click()
    assert InventoryPage(driver).check_inventory_page_open()
