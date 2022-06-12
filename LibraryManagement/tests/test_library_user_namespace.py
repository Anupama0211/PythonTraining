from unittest import mock
import requests_mock
from models.library_model import LibraryModel
from models.user_model import UserModel
from namespaces.library_user_namespace import user_schema


def test_library_get_users_list(client):
    with requests_mock.Mocker() as rm:
        rm.get("http://127.0.0.1:5001/users", json=[{"username": "User"}],
               status_code=200)
        response = client.get("library/users")
        assert response.status_code == 200
        assert response.json == [{"username": "User"}]


def test_post_user(client):
    with requests_mock.Mocker() as rm:
        payload = {"username": "Usersss",
                   "name": "Anupama",
                   "email": "jhaanupama@epam.com"}
        rm.post('http://127.0.0.1:5001/users', json=payload, status_code=201)
        response = client.post("library/users", json=payload)
        assert response.status_code == 201
        assert response.json == payload


def test_library_get_by_username(client):
    with requests_mock.Mocker() as rm:
        rm.get("http://127.0.0.1:5001/users/User",
               json=[{"username": "Users", "name": "Anupama", "email": "jhaanupama@epam.com"}],
               status_code=200)
        library_model_object = LibraryModel("User", 2)
        LibraryModel.find_by_username = mock.Mock(return_value=[library_model_object])
        rm.get("http://127.0.0.1:5001/books/2", json={"id": 2, "name": "Book", "publisher": "ABC", "author": "Author"},
               status_code=200)
        user_object = UserModel()
        user_object.username = "Users"
        user_object.name = "Anupama"
        user_object.email = "jhaanupama@epam.com"
        user_schema.load = mock.Mock(return_value=user_object)
        response = client.get("library/users/User")
        response.json == {'username': 'Users', 'email': 'jhaanupama@epam.com',
                          'books': [{'author': 'Author', 'id': 2, 'name': 'Book', 'publisher': 'ABC'}],
                          'name': 'Anupama'}
        assert response.status_code == 200


def test_library_issue_book(client):
    with requests_mock.Mocker() as rm:
        rm.get("http://127.0.0.1:5001/books/2", json={"id": 2, "name": "Book", "publisher": "ABC", "author": "Author"},
               status_code=200)
        rm.get("http://127.0.0.1:5001/users/User",
               json=[{"username": "Users", "name": "Anupama", "email": "jhaanupama@epam.com"}],
               status_code=200)
        LibraryModel.save_to_db = mock.Mock(return_value=None)
        response = client.post("library/users/User/books/2")
        assert response.json == {'id': None, 'book_id': 2, 'username': 'User'}
        assert response.status_code == 201

# coverage run -m pytest
# coverage report
# coverage html
