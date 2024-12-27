

import pytest
from pages.pet_api import PetAPI
from data.pet_data import generate_pet_data

@pytest.fixture
def create_pet():
    pet_api = PetAPI()
    pet_data = generate_pet_data()
    response = pet_api.create_pet(pet_data)
    assert response.status_code == 200, "Failed to create pet"
    yield pet_data
    pet_api.delete_pet(pet_data["id"])
