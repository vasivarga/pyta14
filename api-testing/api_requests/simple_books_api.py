import requests

from api_requests.generate_token_request import get_token


def get_api_status():
    endpoint = "https://simple-books-api.glitch.me/status"
    response = requests.get(endpoint)
    return response

# print(response)
# print(response.json())
# body = response.json()
# print(body['status'])

def get_list_of_books(book_type="", limit_size=""):
    endpoint = f"https://simple-books-api.glitch.me/books?type={book_type}&limit={limit_size}"
    return requests.get(endpoint)

def get_book_by_id(book_id):
    endpoint = f"https://simple-books-api.glitch.me/books/{book_id}"
    return requests.get(endpoint)

def submit_order(book_id, customer_name):
    endpoint = "https://simple-books-api.glitch.me/orders"

    header_params = {
        'Authorization': f'Bearer {get_token()}'
    }

    request_body = {
        "bookId": book_id,
        "customerName": customer_name
    }

    response = requests.post(endpoint, headers=header_params, json=request_body)
    return response




