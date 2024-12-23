import pytest
from selenium import webdriver
import allure
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
#from selenium.webdriver.opera.options import Options as OperaOptions
#from webdriver_manager.opera import OperaDriverManager
#from selenium.webdriver.opera.service import Service as OperaService

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



@pytest.fixture(scope="session")
def base_url():
    return "http://uitestingplayground.com"

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome, firefox, edge, opera"
    )


@pytest.fixture(scope="function")
def driver(request):

    browser = request.config.getoption("--browser")

    if browser.lower() == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser.lower() == "firefox":
        firefox_options = FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)

    elif browser.lower() == "edge":
        edge_options = EdgeOptions()
        driver = webdriver.Edge(options=edge_options)

    elif browser.lower() == "opera":
        opera_options = OperaOptions()
        driver = webdriver.Opera(options=opera_options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()
