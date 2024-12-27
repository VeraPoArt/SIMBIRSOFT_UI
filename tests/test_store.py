# tests/test_store.py

import pytest
from pages.store_api import StoreAPI
from pages.pet_api import PetAPI
from data.store_data import generate_order_data
from data.pet_data import generate_pet_data
import allure
from datetime import datetime

store_api = StoreAPI()
pet_api = PetAPI()

@allure.feature("Операции с магазином")
class TestStore:


    @allure.testcase("TMS-001", "Создание и проверка заказа через API")
    @allure.title("Создание и верификация заказа для животного")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_and_verify_order(self, create_pet):
        pet_data = create_pet
        pet_id = pet_data["id"]

        order_data = generate_order_data(pet_id)
        with allure.step("Отправить POST запрос для создания заказа"):
            response = store_api.create_order(order_data)
        with allure.step("Проверить статус код создания заказа"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        with allure.step("Проверить данные заказа"):
            json_response = response.json()
            for key in order_data:
                if key == "shipDate":

                    expected_date = datetime.strptime(order_data[key], "%Y-%m-%dT%H:%M:%S.%fZ")
                    actual_date = datetime.strptime(json_response[key], "%Y-%m-%dT%H:%M:%S.%f%z")


                    expected_date = expected_date.replace(microsecond=(expected_date.microsecond // 1000) * 1000)
                    actual_date = actual_date.replace(tzinfo=None,
                                                      microsecond=(actual_date.microsecond // 1000) * 1000)

                    assert expected_date == actual_date, f"Mismatch in {key}: expected {expected_date}, got {actual_date}"
                else:
                    assert json_response[key] == order_data[key], f"Mismatch in {key}"


        order_id = order_data["id"]
        with allure.step("Отправить GET запрос для получения заказа по ID"):
            response = store_api.get_order_by_id(order_id)
        with allure.step("Проверить статус код получения заказа"):
            assert response.status_code == 200
        with allure.step("Проверить данные заказа"):
            json_response = response.json()
            assert json_response["id"] == order_id
            assert json_response["petId"] == pet_id
