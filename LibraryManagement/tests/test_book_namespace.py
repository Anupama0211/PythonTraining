from unittest.mock import Mock

from flask import request

from models.book_model import BookModel
from namespaces.book_namespace import book_schema


def test_get_book_by_id(client):
    BookModel.find_by_id = Mock(return_value={"name": "Book"})
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json == {"name": "Book"}


def test_book_not_found(client):
    BookModel.find_by_id = Mock(return_value=None)
    response = client.get("/books/1")
    print(response.json)
    assert response.status_code == 404
    assert response.json == {
        'message': 'Book not found. You have requested this URI [/books/1] but did you mean /books/<book_id> or /books or /library/books/<book_id> ?'}


def test_get_books_list(client):
    BookModel.find_all = Mock(return_value=[{"name": "Book"}])
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json == [{"name": "Book"}]


def test_post_book(client):
    payload = {"name": "Book"}
    book_object = BookModel()
    book_object.name = "Book"
    book_schema.load = Mock(return_value=book_object)
    BookModel.save_to_db = Mock(return_value=None)
    book_schema.dump = Mock(return_value=payload)
    response = client.post("/books", json=payload)
    assert response.status_code == 201
    assert response.json == payload
    BookModel.save_to_db.assert_called_once()

# coverage run -m pytest
# coverage report
# coverage html
