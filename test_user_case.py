import time

import pytest
from pages import LoginPage, InventoryPage, CheckoutCompletePage, CheckoutOverviewPage, CheckoutPage, CartPage
import allure

@allure.testcase("TMS-007", "Пользовательский сценарий 001")
@allure.title("Пользовательский сценарий 001")
@allure.severity(allure.severity_level.NORMAL)
def test_user_case_001(driver):
    """
       Тестовый сценарий:
           1. Авторизация на сайте.
           2. Добавление товара Sauce Labs Backpack в корзину.
           3. Проверка количества товаров в корзине.
           4. Переход в корзину.
           5. Проверка деталей товара в корзине.
           6. Оформление заказа.
           7. Проверка деталей заказа на этапе обзора.
           8. Завершение заказа.
           9. Проверка страницы завершения заказа.
       """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

    with allure.step("Авторизация как стандартный пользователь"):
        login_page.input_login('standard_user')
        login_page.input_password('secret_sauce')
        login_page.login_button_click()
        assert inventory_page.check_inventory_page_open(), "Страница инвентаря не открыта после авторизации."
        time.sleep(3)

    with allure.step("Сохранить цену Sauce Labs Backpack перед добавлением в корзину"):
        backpack_price_text = inventory_page.get_item_price("Sauce Labs Backpack")
        backpack_price = float(backpack_price_text.replace("$", ""))
        allure.attach(backpack_price_text, name="Цена Sauce Labs Backpack", attachment_type=allure.attachment_type.TEXT)
        time.sleep(3)

    with allure.step("Добавить Sauce Labs Backpack в корзину"):
        inventory_page.add_backpack_to_cart()
        time.sleep(3)

    with allure.step("Проверить, что рядом с иконкой корзины появилась цифра 1"):
        cart_quantity = inventory_page.get_cart_quantity()
        assert cart_quantity == "1", f"Ожидалось количество в корзине: 1, получено: {cart_quantity}"
        allure.attach(cart_quantity, name="Количество товаров в корзине", attachment_type=allure.attachment_type.TEXT)
        time.sleep(3)

    with allure.step("Перейти в корзину"):
        inventory_page.go_to_cart()
        assert cart_page.check_cart_page_open(), "Страница корзины не открыта."
        time.sleep(3)

    with allure.step("Проверить, что в корзине 1 товар"):
        cart_items = cart_page.get_cart_items()
        assert len(cart_items) == 1, f"Ожидалось 1 товар в корзине, найдено: {len(cart_items)}"
        time.sleep(3)

    with allure.step("Проверить количество единиц товара - 1"):
        quantity_text = cart_page.get_item_quantity()
        assert quantity_text == "1", f"Ожидалось количество: 1, получено: {quantity_text}"
        time.sleep(3)

    with allure.step("Проверить название товара - Sauce Labs Backpack"):
        item_name = cart_page.get_item_name()
        assert "Sauce Labs Backpack" in item_name, f"Название товара не соответствует. Ожидалось: 'Sauce Labs Backpack', получено: '{item_name}'"
        time.sleep(3)

    with allure.step("Проверить цену товара в корзине"):
        item_price_text = cart_page.get_item_price()
        item_price = float(item_price_text.replace("$", ""))
        assert item_price == backpack_price, f"Цена товара в корзине не совпадает с ценой на странице товара. Ожидалось: {backpack_price}, получено: {item_price}"
        time.sleep(3)

    with allure.step("Нажать кнопку Checkout"):
        cart_page.checkout()
        assert checkout_page.check_checkout_overview_page_open(), "Страница оформления заказа не открыта."
        time.sleep(3)

    with allure.step("Заполнить данные для оформления заказа"):
        checkout_page.fill_checkout_info("Joe", "Lowson", "1234")
        assert checkout_overview_page.check_checkout_overview_page_open(), "Страница обзора заказа не открыта."
        time.sleep(3)

    with allure.step("Проверить, что в обзоре заказа 1 товар"):
        overview_items = checkout_overview_page.get_overview_items()
        assert len(overview_items) == 1, f"Ожидалось 1 товар в обзоре заказа, найдено: {len(overview_items)}"
        time.sleep(3)

    with allure.step("Проверить название товара в обзоре заказа - Sauce Labs Backpack"):
        overview_item = overview_items[0]
        overview_item_name = checkout_overview_page.get_item_name(overview_item)
        assert "Sauce Labs Backpack" in overview_item_name, f"Название товара в обзоре заказа не соответствует. Ожидалось: 'Sauce Labs Backpack', получено: '{overview_item_name}'"
        time.sleep(3)

    with allure.step("Проверить цену товара в обзоре заказа"):
        overview_item_price_text = checkout_overview_page.get_item_price(overview_item)
        overview_item_price = float(overview_item_price_text.replace("$", ""))
        assert overview_item_price == backpack_price, f"Цена товара в обзоре заказа не совпадает с ценой на странице товара. Ожидалось: {backpack_price}, получено: {overview_item_price}"
        time.sleep(3)

    with allure.step("Проверить информацию о платеже"):
        payment_label = checkout_overview_page.get_payment_info_label()
        assert "Payment Information:" in payment_label, "Заголовок Payment Information отсутствует или некорректен."
        payment_value = checkout_overview_page.get_payment_info_value()
        assert "SauceCard #31337" in payment_value, "Значение Payment Information некорректно."
        time.sleep(3)

    with allure.step("Проверить информацию о доставке"):
        shipping_label = checkout_overview_page.get_shipping_info_label()
        assert "Shipping Information:" in shipping_label, "Заголовок Shipping Information отсутствует или некорректен."
        shipping_value = checkout_overview_page.get_shipping_info_value()
        assert "Free Pony Express Delivery!" in shipping_value, "Значение Shipping Information некорректно."
        time.sleep(3)

    with allure.step("Проверить итоговую цену"):
        item_total = checkout_overview_page.get_item_total()
        tax = checkout_overview_page.get_tax()
        expected_total = item_total + tax
        actual_total = checkout_overview_page.get_total()
        assert actual_total == expected_total, f"Total не совпадает. Ожидалось: {expected_total}, получено: {actual_total}"
        time.sleep(3)

    with allure.step("Завершить оформление заказа"):
        checkout_overview_page.finish_checkout()
        assert checkout_complete_page.check_checkout_complete_page_open(), "Страница завершения заказа не открыта."
        time.sleep(3)

    with allure.step("Проверить заголовок завершения заказа - Checkout: Complete!"):
        title = checkout_complete_page.get_title()
        assert "Checkout: Complete!" in title, f"Заголовок 'Checkout: Complete!' отсутствует. Получено: '{title}'"
        time.sleep(3)

    with allure.step("Проверить заголовок благодарности - Thank you for your order!"):
        complete_header = checkout_complete_page.get_complete_header()
        assert "Thank you for your order!" in complete_header, f"Заголовок 'Thank you for your order!' отсутствует. Получено: '{complete_header}'"

    with allure.step("Проверить текст о доставке"):
        complete_text = checkout_complete_page.get_complete_text()
        expected_text = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
        assert expected_text in complete_text, f"Текст о доставке отсутствует или некорректен. Ожидалось: '{expected_text}', получено: '{complete_text}'"

    with allure.step("Проверить наличие кнопки Back Home"):
        back_home_displayed = checkout_complete_page.is_back_home_button_displayed()
        assert back_home_displayed, "Кнопка 'Back Home' отсутствует на странице."