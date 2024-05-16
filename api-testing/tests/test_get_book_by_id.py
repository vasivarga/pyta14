import unittest

from api_requests.simple_books_api import get_book_by_id


class TestGetBookById(unittest.TestCase):

    def test_get_book_by_valid_id(self):
        response = get_book_by_id(5)

        assert response.status_code == 200, "Unexpected status code"
        assert response.json()['id'] == 5, "Unexpected book id"

    #Tema: def test_get_book_by_invalid_id(self):