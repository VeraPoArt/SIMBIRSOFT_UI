import allure
import requests
from utils.config import BASE_URL

class StoreAPI:
    def __init__(self):
        self.base_url = f"{BASE_URL}/store"

    @allure.step("Создание заказа")
    def create_order(self, order_data):
        response = requests.post(f"{self.base_url}/order", json=order_data)
        return response

    @allure.step("Получение заказа по ID: {order_id}")
    def get_order_by_id(self, order_id):
        response = requests.get(f"{self.base_url}/order/{order_id}")
        return response
