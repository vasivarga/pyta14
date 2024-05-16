import random

import requests


def get_token():
    endpoint = "https://simple-books-api.glitch.me/api-clients/"

    random_number = random.randint(1, 999999999999999999999)

    request_body = {
        "clientName": "Postman",
        "clientEmail": f"pyta14_itf{random_number}@gmail.com"
    }
    response = requests.post(endpoint, json=request_body)
    token = response.json()['accessToken']
    return token