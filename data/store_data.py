

import random
from datetime import datetime

def generate_order_data(pet_id):
    order_id = random.randint(100000, 999999)
    ship_date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    return {
        "id": order_id,
        "petId": pet_id,
        "quantity": 1,
        "shipDate": ship_date,
        "status": "placed",
        "complete": True
    }
