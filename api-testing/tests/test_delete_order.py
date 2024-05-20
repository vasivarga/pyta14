import unittest

from api_requests.simple_books_api import submit_order, delete_order, get_order


class TestDeleteOrder:

    def test_delete_order(self):
        order_response = submit_order(1, "Test User")
        order_id = order_response.json()['orderId']

        delete_response = delete_order(order_id)
        assert delete_response.status_code == 204

        get_order_response = get_order(order_id)
        expected_error_text = f"No order with id {order_id}."
        actual_error_text = get_order_response.json()['error']

        assert expected_error_text == actual_error_text
