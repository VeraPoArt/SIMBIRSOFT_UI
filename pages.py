from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure



class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(driver, timeout)
        self.page_url = ''

    @allure.step("Поиск элемента с локатором: {by}, значение: {value}")
    def find_element(self, by: By or int, value: str) -> WebElement:
        return self.wait.until(expected_conditions.visibility_of_element_located((by, value)),
                               message=f'Элемент {by, value} не найден')

    @allure.step("Поиск всех элементов с локатором: {by}, значение: {value}")
    def find_elements(self, by: By or int, value: str) -> [WebElement]:
        return self.wait.until(expected_conditions.visibility_of_all_elements_located((by, value)),
                               message=f'Элементы {by, value} не найдены')

    @allure.step("Получение текущего URL страницы")
    def get_current_url(self) -> str:
        return self.driver.current_url


class LoginPage(BasePage):

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

    @allure.step("Ввод логина: {login}")
    def input_login(self, login: str) -> None:
        self.find_element(*self.login).send_keys(login)

    @allure.step("Ввод пароля: {password}")
    def input_password(self, password: str) -> None:
        self.find_element(*self.password).send_keys(password)


    @allure.step("Нажатие кнопки Login")
    def login_button_click(self) -> None:
        self.find_element(*self.login_btn).click()

    @allure.step("Проверка, что страница логина открыта")
    def check_login_page_open(self) -> bool:
        return self.get_current_url() == self.page_url

    @allure.step("Получение текста сообщения об ошибке")
    def get_error_message(self) -> str:
        return self.find_element(*self.error_message).text

    @allure.step("Получение значения атрибута '{attribute_name}' для элемента с локатором {locator}")
    def get_attribute(self, locator, attribute_name: str) -> str:
        element = self.find_element(*locator)
        return element.get_attribute(attribute_name)


class InventoryPage(BasePage):
    def __init__(self, driver):
        """
        Локаторы для страницы товаров.

        Атрибуты:
            BACKPACK_ADD_BUTTON (tuple): Локатор кнопки "Add to cart" для Sauce Labs Backpack.
            CART_BADGE (tuple): Локатор элемента, отображающего количество товаров в корзине.
            CART_LINK (tuple): Локатор ссылки на корзину.
            INVENTORY_ITEM (tuple): Локатор контейнера товара.
            INVENTORY_ITEM_NAME (tuple): Локатор названия товара.
            INVENTORY_ITEM_PRICE (tuple): Локатор цены товара.
            CHECKOUT_BUTTON (tuple): Локатор кнопки "Checkout".
        """
        super().__init__(driver, timeout=60)
        self.page_url = 'https://www.saucedemo.com/inventory.html'
        self.BACKPACK_ADD_BUTTON = (By.CSS_SELECTOR, "*[data-test='add-to-cart-sauce-labs-backpack']")
        self.CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
        self.CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        self.INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
        self.INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
        self.INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
        self.CHECKOUT_BUTTON = (By.ID, "checkout")
    @allure.step("Проверка, что открыта страница инвентаря")
    def check_inventory_page_open(self) -> bool:
        return self.get_current_url() == self.page_url
    @allure.step("Добавить Товар в корзину")
    def add_backpack_to_cart(self):
        self.find_element(*self.BACKPACK_ADD_BUTTON).click()

    @allure.step("Получить количество товаров в корзине")
    def get_cart_quantity(self) -> str:
        return self.find_element(*self.CART_BADGE).text

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        cart_link_element = self.find_element(*self.CART_LINK)
        cart_link_element.click()

    @allure.step("Получить цену товара {item_name}")
    def get_item_price(self, item_name: str) -> str:
        item = self.find_element(By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']")
        price = item.find_element(*self.INVENTORY_ITEM_PRICE).text
        return price


class CartPage(BasePage):
    """
    Класс для работы со страницей корзины.

    Локаторы:
        CART_ITEMS (tuple): Локатор контейнеров всех товаров в корзине.
        CART_ITEM_NAME (tuple): Локатор названия товара в корзине.
        CART_ITEM_PRICE (tuple): Локатор цены товара в корзине.
        CART_ITEM_QUANTITY (tuple): Локатор количества товара в корзине.
        CHECKOUT_BUTTON (tuple): Локатор кнопки "Checkout".
        PAGE_URL (str): URL страницы корзины.
    """

    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.page_url = 'https://www.saucedemo.com/cart.html'
        self.CART_ITEMS = (By.CLASS_NAME, "cart_item")
        self.CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
        self.CART_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
        self.CART_ITEM_QUANTITY = (By.CLASS_NAME, "cart_quantity")
        self.CHECKOUT_BUTTON = (By.ID, "checkout")


    @allure.step("Получить все товары в корзине")
    def get_cart_items(self) -> list:
        return self.find_elements(*self.CART_ITEMS)

    @allure.step("Получить название товара в корзине")
    def get_item_name(self) -> str:
        return self.find_element(*self.CART_ITEM_NAME).text

    @allure.step("Получить цену товара в корзине")
    def get_item_price(self) -> str:
        return self.find_element(*self.CART_ITEM_PRICE).text

    @allure.step("Получить количество товара в корзине")
    def get_item_quantity(self) -> str:
        return self.find_element(*self.CART_ITEM_QUANTITY).text

    @allure.step("Нажать кнопку Checkout")
    def checkout(self):
        self.find_element(*self.CHECKOUT_BUTTON).click()

        # pages/cart_page.py

    @allure.step("Проверка, что открыта страница корзины")
    def check_cart_page_open(self) -> bool:
        return self.get_current_url() == self.page_url


class CheckoutPage(BasePage):
    """
    Класс для работы со страницей оформления заказа.

    Локаторы:
        FIRST_NAME_INPUT (tuple): Локатор поля ввода имени.
        LAST_NAME_INPUT (tuple): Локатор поля ввода фамилии.
        POSTAL_CODE_INPUT (tuple): Локатор поля ввода почтового кода.
        CONTINUE_BUTTON (tuple): Локатор кнопки "Continue".
        PAGE_URL (str): URL страницы оформления заказа.
    """

    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.page_url = 'https://www.saucedemo.com/checkout-step-one.html'
        self.FIRST_NAME_INPUT = (By.ID, "first-name")
        self.LAST_NAME_INPUT = (By.ID, "last-name")
        self.POSTAL_CODE_INPUT = (By.ID, "postal-code")
        self.CONTINUE_BUTTON = (By.ID, "continue")

    @allure.step("Ввести имя: {first_name}")
    def input_first_name(self, first_name: str):
        self.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

    @allure.step("Ввести фамилию: {last_name}")
    def input_last_name(self, last_name: str):
        self.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    @allure.step("Ввести почтовый код: {postal_code}")
    def input_postal_code(self, postal_code: str):
        self.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)

    @allure.step("Нажать кнопку Continue")
    def continue_button_click(self):
        self.find_element(*self.CONTINUE_BUTTON).click()

    @allure.step("Заполнить данные для оформления заказа")
    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_postal_code(postal_code)
        self.continue_button_click()

    @allure.step("Проверка, что открыта страница обзора заказа")
    def check_checkout_overview_page_open(self) -> bool:
        return self.get_current_url() == 'https://www.saucedemo.com/checkout-step-one.html'

    @allure.step("Проверка, что открыта страница обзора заказа")
    def check_checkout_overview_page_open(self) -> bool:
        """
        Проверяет, что текущий URL соответствует странице обзора заказа.

        Returns:
            bool: True, если URL совпадает, иначе False.
        """
        current_url = self.get_current_url()
        is_open = current_url == self.page_url
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)
        return is_open


class CheckoutOverviewPage(BasePage):
    """
    Класс для работы со страницей обзора заказа.

    Локаторы:
        OVERVIEW_ITEMS (tuple): Локатор контейнеров всех товаров в обзоре заказа.
        ITEM_TOTAL_LABEL (tuple): Локатор метки с общей стоимостью товаров.
        TAX_LABEL (tuple): Локатор метки с налогом.
        TOTAL_LABEL (tuple): Локатор метки с итоговой суммой.
        FINISH_BUTTON (tuple): Локатор кнопки "Finish".
        PAYMENT_INFO_LABEL (tuple): Локатор метки с информацией о платеже.
        SHIPPING_INFO_LABEL (tuple): Локатор метки с информацией о доставке.
        PAGE_URL (str): URL страницы обзора заказа.
    """

    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.page_url = 'https://www.saucedemo.com/checkout-step-two.html'
        self.OVERVIEW_ITEMS = (By.CLASS_NAME, "cart_item")
        self.ITEM_TOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
        self.TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")
        self.TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
        self.FINISH_BUTTON = (By.ID, "finish")
        self.PAYMENT_INFO_LABEL = (By.XPATH, "//div[@class='summary_info_label' and text()='Payment Information:']")
        self.PAYMENT_INFO_VALUE = (By.XPATH,
                              "//div[@class='summary_info_label' and text()='Payment Information:']/following-sibling::div[@class='summary_value_label']")
        self.SHIPPING_INFO_LABEL = (By.XPATH, "//div[@class='summary_info_label' and text()='Shipping Information:']")
        self.SHIPPING_INFO_VALUE = (By.XPATH,
                               "//div[@class='summary_info_label' and text()='Shipping Information:']/following-sibling::div[@class='summary_value_label']")

    @allure.step("Получить все товары в обзоре заказа")
    def get_overview_items(self) -> list:
        return self.find_elements(*self.OVERVIEW_ITEMS)

    @allure.step("Получить название товара в обзоре заказа")
    def get_item_name(self, item: WebElement) -> str:
        return item.find_element(By.CLASS_NAME, "inventory_item_name").text

    @allure.step("Получить цену товара в обзоре заказа")
    def get_item_price(self, item: WebElement) -> str:
        return item.find_element(By.CLASS_NAME, "inventory_item_price").text

    @allure.step("Получить сумму товаров")
    def get_item_total(self) -> float:
        text = self.find_element(*self.ITEM_TOTAL_LABEL).text
        return float(text.replace("Item total: $", ""))

    @allure.step("Получить сумму налога")
    def get_tax(self) -> float:
        text = self.find_element(*self.TAX_LABEL).text
        return float(text.replace("Tax: $", ""))

    @allure.step("Получить отображаемую общую сумму")
    def get_total(self) -> float:
        text = self.find_element(*self.TOTAL_LABEL).text
        return float(text.replace("Total: $", ""))

    @allure.step("Рассчитать ожидаемую общую сумму (Item total + Tax)")
    def calculate_expected_total(self) -> float:
        item_total = self.get_item_total()
        tax = self.get_tax()
        expected_total = round(item_total + tax, 2)
        allure.attach(str(expected_total), name="Рассчитанная ожидаемая сумма",
                      attachment_type=allure.attachment_type.TEXT)
        return expected_total

    @allure.step("Нажать кнопку Finish")
    def finish_checkout(self):
        self.find_element(*self.FINISH_BUTTON).click()

    @allure.step("Получить текст заголовка информации о платеже")
    def get_payment_info_label(self) -> str:
        return self.find_element(*self.PAYMENT_INFO_LABEL).text

    @allure.step("Получить значение информации о платеже")
    def get_payment_info_value(self) -> str:
        return self.find_element(*self.PAYMENT_INFO_VALUE).text

    @allure.step("Получить текст заголовка информации о доставке")
    def get_shipping_info_label(self) -> str:
        return self.find_element(*self.SHIPPING_INFO_LABEL).text

    @allure.step("Получить значение информации о доставке")
    def get_shipping_info_value(self) -> str:
        return self.find_element(*self.SHIPPING_INFO_VALUE).text

    def check_checkout_overview_page_open(self) -> bool:
        current_url = self.get_current_url()
        is_open = current_url == self.page_url
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)
        return is_open


class CheckoutCompletePage(BasePage):
    """
    Класс для работы со страницей завершения заказа.

    Локаторы:
        COMPLETE_HEADER (tuple): Локатор заголовка завершения заказа.
        COMPLETE_TEXT (tuple): Локатор текста завершения заказа.
        BACK_HOME_BUTTON (tuple): Локатор кнопки "Back Home".
        TITLE (tuple): Локатор заголовка страницы.
        PAGE_URL (str): URL страницы завершения заказа.
    """

    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.page_url = 'https://www.saucedemo.com/checkout-complete.html'
        self.COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
        self.COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
        self.BACK_HOME_BUTTON = (By.ID, "back-to-products")
        self.TITLE = (By.CLASS_NAME, "title")

    @allure.step("Получить заголовок завершения заказа")
    def get_complete_header(self) -> str:
        return self.find_element(*self.COMPLETE_HEADER).text

    @allure.step("Получить текст завершения заказа")
    def get_complete_text(self) -> str:
        return self.find_element(*self.COMPLETE_TEXT).text

    @allure.step("Нажать кнопку Back Home")
    def back_home(self):
        self.find_element(*self.BACK_HOME_BUTTON).click()

    @allure.step("Получить заголовок страницы")
    def get_title(self) -> str:
        return self.find_element(*self.TITLE).text


    @allure.step("Проверка, что открыта страница завершения заказа")
    def check_checkout_complete_page_open(self) -> bool:
        current_url = self.get_current_url()
        is_open = current_url == self.page_url
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)
        return is_open

    @allure.step("Проверить отображение кнопки Back Home")
    def is_back_home_button_displayed(self) -> bool:
        try:
            button = self.find_element(*self.BACK_HOME_BUTTON)
            is_displayed = button.is_displayed()
            allure.attach(str(is_displayed), name="Отображается кнопка Back Home", attachment_type=allure.attachment_type.TEXT)
            return is_displayed
        except NoSuchElementException:
            allure.attach("Кнопка Back Home не найдена.", name="Back Home Button Missing", attachment_type=allure.attachment_type.TEXT)
            return False