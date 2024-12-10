from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(driver, timeout)
        self.page_url = ''

    def find_element(self, by: By or int, value: str) -> WebElement:
        return self.wait.until(expected_conditions.visibility_of_element_located((by, value)),
                               message=f'Элемент {by, value} не найден')

    def find_elements(self, by: By or int, value: str) -> [WebElement]:
        return self.wait.until(expected_conditions.visibility_of_all_elements_located((by, value)),
                               message=f'Элементы {by, value} не найдены')

    def get_current_url(self) -> str:
        return self.driver.current_url


class LoginPage(BasePage):
    """
    Класс для работы со страницей логина.

    Методы:
        __init__(driver):
            Инициализация драйвера и элементов страницы.
    """

    def __init__(self, driver):
        """
        Локаторы для страницы логина.

        Атрибуты:
            login (tuple): Локатор строки ввода логина.
            password (tuple): Локатор строки ввода пароля.
            login_button (tuple): Локатор кнопки логина.
            error_message (tuple): Локатор для отображения сообщений об ошибке.
            page_url (str): URL страницы логина.
        """
        super().__init__(driver, timeout=60)
        self.login = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.login_btn = (By.NAME, 'login-button')
        self.error_message = (By.CSS_SELECTOR, '[data-test="error"]')
        self.page_url = 'https://www.saucedemo.com/'

    def input_login(self, login: str) -> None:
        self.find_element(*self.login).send_keys(login)

    def input_password(self, password: str) -> None:
        self.find_element(*self.password).send_keys(password)

    def login_button_click(self) -> None:
        self.find_element(*self.login_btn).click()

    def check_login_page_open(self) -> bool:
        return self.get_current_url() == self.page_url

    def get_error_message(self) -> str:
        return self.find_element(*self.error_message).text

    def get_attribute(self, locator, attribute_name: str) -> str:
        element = self.find_element(*locator)
        return element.get_attribute(attribute_name)


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.page_url = 'https://www.saucedemo.com/inventory.html'

    def check_inventory_page_open(self) -> bool:
        return self.get_current_url() == self.page_url
