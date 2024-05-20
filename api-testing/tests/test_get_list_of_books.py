import unittest

from api_requests.simple_books_api import get_list_of_books


class TestGetListOfBooks:

    def test_get_list_of_books_without_filter(self):

        response = get_list_of_books()
        assert response.status_code == 200, "Unexpected status code"

        body = response.json()

        assert len(body) == 6, "Unexpected number of books returned"

        # print(body)
        #
        # for book in body:
        #     print(book['id'])
        #     print(book['name'])
        #     print(book['type'])
        #     print(book['available'])
        #     print("-------------------")

    def test_get_list_of_books_filet_by_type(self):
        response = get_list_of_books("fiction")
        body = response.json()

        assert response.status_code == 200, "Unexpected status code"

        assert len(body) == 4, "Unexpected book list size"

        for book in body:
            assert book['type'] == "fiction"

    def test_get_list_of_books_filter_by_limit(self):
        response = get_list_of_books(limit_size=2)
        body = response.json()

        assert response.status_code == 200, "Unexpected status code"
        assert len(body), "Unexpected list size returned"

    def test_get_list_of_books_filter_by_invalid_limit_less_than_0(self):
        response = get_list_of_books(limit_size=-5)

        assert response.status_code == 400, "Unexpected status code"

        expected_error_message = "Invalid value for query parameter 'limit'. Must be greater than 0."
        actual_error_message = response.json()['error']

        assert expected_error_message == actual_error_message, "Unexpected error message"


    # Tema: def test_get_list_of_books_filter_by_invalid_limit_greater_than_20(self):
    # Tema: def test_get_list_of_filter_by_type_and_limit(self):
    # Tema: def test_get_list_of_filter_by_invalid_type(self):