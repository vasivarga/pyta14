import unittest

from api_requests.simple_books_api import submit_order, update_order, get_order


class TestUpdateOrder:

    def test_update_order_with_valid_order_id(self):
        book_id = 1
        customer_name = "Py Ta 14"
        submit_order_response = submit_order(book_id, customer_name)

        # Comanda plasata initial are id-ul de mai jos:
        submit_order_id = submit_order_response.json()['orderId']

        new_customer_name = "Pyta14 Automation"

        # Actualizam comanda cu un nou nume
        update_order_response = update_order(submit_order_id, new_customer_name)

        assert update_order_response.status_code == 204

        get_order_response = get_order(submit_order_id)
        actual_new_name = get_order_response.json()['customerName']

        assert actual_new_name == new_customer_name

