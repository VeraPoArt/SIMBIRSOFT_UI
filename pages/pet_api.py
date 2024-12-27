import allure
import requests
from utils.config import BASE_URL

class PetAPI:
    def __init__(self):
        self.base_url = f"{BASE_URL}/pet"

    @allure.step("Создание питомца с данными: {pet_data}")
    def create_pet(self, pet_data):
        response = requests.post(f"{self.base_url}", json=pet_data)
        return response

    @allure.step("Получение питомца по ID: {pet_id}")
    def get_pet_by_id(self, pet_id):
        response = requests.get(f"{self.base_url}/{pet_id}")
        return response

    @allure.step("Обновление данных питомца: {pet_data}")
    def update_pet(self, pet_data):
        response = requests.put(f"{self.base_url}", json=pet_data)
        return response

    @allure.step("Удаление питомца по ID: {pet_id}")
    def delete_pet(self, pet_id):
        response = requests.delete(f"{self.base_url}/{pet_id}")
        return response
