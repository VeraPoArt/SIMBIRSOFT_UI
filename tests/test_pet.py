import allure

from data.pet_data import generate_pet_data
from pages.pet_api import PetAPI

pet_api = PetAPI()

@allure.feature("CRUD операции с животными")
class TestPet:

    @allure.testcase("TMS-001", "Создание животного")
    @allure.title("Создание нового животного через API")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_pet(self):
        pet_data = generate_pet_data()
        with allure.step("Отправить POST запрос для создания животного"):
            response = pet_api.create_pet(pet_data)
        with allure.step("Проверить статус код"):
            assert response.status_code == 200
        with allure.step("Проверить данные животного"):
            json_response = response.json()
            for key in pet_data:
                assert json_response[key] == pet_data[key]


    @allure.testcase("TMS-002", "Получение животного по ID")
    @allure.title("Получение данных о животном через GET запрос")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_pet_by_id(self):
        pet_data = generate_pet_data()
        pet_api.create_pet(pet_data)
        pet_id = pet_data["id"]
        with allure.step("Отправить GET запрос для получения животного по ID"):
            response = pet_api.get_pet_by_id(pet_id)
        with allure.step("Проверить статус код"):
            assert response.status_code == 200
        with allure.step("Проверить данные животного"):
            json_response = response.json()
            assert json_response["id"] == pet_id


    @allure.testcase("TMS-003", "Обновление животного")
    @allure.title("Обновление данных животного через PUT запрос")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_pet(self):
        pet_data = generate_pet_data()
        pet_api.create_pet(pet_data)
        pet_data["name"] = "UpdatedName"
        with allure.step("Отправить PUT запрос для обновления животного"):
            response = pet_api.update_pet(pet_data)
        with allure.step("Проверить статус код"):
            assert response.status_code == 200
        with allure.step("Проверить обновленные данные"):
            json_response = response.json()
            assert json_response["name"] == "UpdatedName"


    @allure.testcase("TMS-004", "Удаление животного")
    @allure.title("Удаление животного через DELETE запрос")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_pet(self):
        pet_data = generate_pet_data()
        pet_api.create_pet(pet_data)
        pet_id = pet_data["id"]
        with allure.step("Отправить DELETE запрос для удаления животного"):
            response = pet_api.delete_pet(pet_id)
        with allure.step("Проверить статус код"):
            assert response.status_code == 200
        with allure.step("Проверить, что животное удалено"):
            response = pet_api.get_pet_by_id(pet_id)
            assert response.status_code == 404

    @allure.testcase("TMS-005", "Создание животного с некорректными данными")
    @allure.title("Негативный сценарий: Создание животного с некорректным типом данных")
    @allure.severity(allure.severity_level.MINOR)
    def test_create_pet_negative(self):
        invalid_pet_data = {
            "id": "invalid_id",
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "TestPet",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        with allure.step("Отправить POST запрос для создания животного с некорректным типом данных"):
            response = pet_api.create_pet(invalid_pet_data)
        with allure.step("Проверить статус код"):
            assert response.status_code == 500, f"Expected 500, got {response.status_code}"
        with allure.step("Проверить наличие сообщения об ошибке"):
            json_response = response.json()
            assert "message" in json_response, "Поле 'message' отсутствует в ответе"
