import unittest
from unittest.mock import Mock, patch

from models.book_model import BookModel


def test_get_book_by_id(client):
    BookModel.find_by_id = Mock(return_value={"name": "Book"})
    response = client.get("/books/1")
    print(response.data)
    assert response.status_code == 200


def test_book_not_found(client):
    BookModel.find_by_id = Mock(return_value=None)
    response = client.get("/books/1")
    print(response.data)
    assert response.status_code == 404


def test_books_list(client):
    BookModel.find_all = Mock(return_value=[{"name": "Book"}])
    response = client.get("/books")
    print(response.data)
    assert response.status_code == 200
