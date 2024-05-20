import unittest

from api_requests.simple_books_api import submit_order, get_order


class TestGetSingleOrder:

    def test_get_single_oder_with_valid_order_id(self):
        order_response = submit_order(1, "Test User")
        order_id = order_response.json()['orderId']

        get_order_response = get_order(order_id)
        assert get_order_response.status_code == 200
        assert order_id == get_order_response.json()['id']

    # Tema: def test_get_single_ordrer_with_invalid_order_id(self):
                        # get_order_response = get_order("sdfsdfdsfsd")
