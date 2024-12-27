import random

def generate_pet_data():
    pet_id = random.randint(100000, 999999)
    return {
        "id": pet_id,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Doggie",
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


