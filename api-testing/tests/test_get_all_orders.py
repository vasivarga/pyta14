import unittest

from api_requests.simple_books_api import submit_order, get_all_orders


class TestGetAllOrders:

    def test_get_all_orders(self):
        book_id = 1
        customer_name = "Py Ta 14"
        submit_order_response = submit_order(book_id, customer_name)

        # Dictionar
        submit_order_body = submit_order_response.json()

        submit_order_id = submit_order_body['orderId']

        get_orders_response = get_all_orders()

        # Lista
        get_orders_body = get_orders_response.json()

        get_orders_id = get_orders_body[0]['id']

        assert submit_order_id == get_orders_id
        assert len(get_orders_response.json()) == 1
        assert get_orders_response.status_code == 200
