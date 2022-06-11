from unittest.mock import Mock

from models.user_model import UserModel
from schemas import user_schema


def test_get_by_username(client):
    UserModel.find_by_username = Mock(return_value={"username": "User"})
    response = client.get("/users/User")
    assert response.status_code == 200
    assert response.json == {"username": "User"}


def test_user_not_found(client):
    UserModel.find_by_username = Mock(return_value=None)
    response = client.get("/users/User")
    print(response.json)
    assert response.status_code == 404
    assert response.json == {
        'message': 'User not found. You have requested this URI [/users/User] but did you mean /users/<username> or /users ?'}


def test_get_users_list(client):
    UserModel.find_all = Mock(return_value=[{"username": "User"}])
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json == [{"username": "User"}]


def test_post_user(client):
    payload = {"username": "Usersss", "name": "Anupama", "email": "jhaanupama@epam.com"}
    user_object = UserModel()
    user_object.username = "Usersss"
    user_object.name = "Anupama"
    user_object.email = "jhaanupama@epam.com"
    user_schema.load = Mock(return_value=user_object)
    UserModel.save_to_db = Mock(return_value=None)
    user_schema.dump = Mock(return_value=payload)
    response = client.post("/users", json=payload)
    assert response.status_code == 201
    assert response.json == payload
    user_object.save_to_db.assert_called_once()


def test_post_user_raise_validation_error(client):
    payload = {"username": "Use", "name": "Anupama", "email": "jhaanupama@epam.com"}
    user_object = UserModel()
    user_object.username = "Use"
    user_object.name = "Anupama"
    user_object.email = "jhaanupama@epam.com"
    user_schema.load = Mock(return_value=user_object)
    UserModel.save_to_db = Mock(return_value=None)
    user_schema.dump = Mock(return_value=payload)
    response = client.post("/users", json=payload)
    assert response.status_code == 400
    assert response.json == {"errors": {"username": "\'Use\' is too short"},
                             "message": "Input payload validation failed"}

# coverage run -m pytest
# coverage report
# coverage html
