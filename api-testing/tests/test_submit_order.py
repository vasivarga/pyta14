import unittest

from api_requests.simple_books_api import submit_order


class TestSubmitOrder:

    def test_submit_valid_order(self):
        book_id = 1
        customer_name = "Py Ta 14"

        response = submit_order(book_id, customer_name)

        assert response.status_code == 201, "Unexpected status code"
        assert response.json()["created"], "Order was not submitted"
