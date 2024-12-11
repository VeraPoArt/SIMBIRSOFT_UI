from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import allure

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--enable-javascript')
    _driver = webdriver.Chrome(options=options)
    _driver.get('https://www.saucedemo.com/')
    yield _driver
    _driver.quit()



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )

