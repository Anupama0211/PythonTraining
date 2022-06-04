import requests
from flask import request
from flask_restx import Resource, Namespace, fields

from models.library_model import LibraryModel
from namespaces.user_namespace import user
from schemas.library_schema import LibrarySchema
from schemas.user_schema import UserSchema
from schemas.book_schema import BookSchema

from db import db

library_user_ns = Namespace("library/users", description="Library user related operations")
library_user_schema = LibrarySchema()
library_users_schema = LibrarySchema(many=True)
user_schema = UserSchema()
book_schema = BookSchema()

URL_USERS = "http://127.0.0.1:5000/users"
URL_BOOKS = "http://127.0.0.1:5000/books"

library = library_user_ns.model('Library ', {
    'id': fields.Integer("Id"),
    'username': fields.String("UserName"),
    'book_id': fields.String("Book ID"),
})


@library_user_ns.route("/")
class LibraryUsers(Resource):
    @library_user_ns.response(200, "Successful", model=[user])
    def get(self):
        response = requests.get(URL_USERS)
        return response.json(), response.status_code

    @library_user_ns.expect(user, validate=True)
    @library_user_ns.response(201, "Successful", model=user)
    @library_user_ns.response(400, "Bad Request")
    def post(self):
        user_json = request.get_json()
        return requests.post(URL_USERS, json=user_json).json(), 201


@library_user_ns.route("/<username>")
class LibraryUser(Resource):
    @library_user_ns.response(200, "Successful", model=user)
    @library_user_ns.response(404, "Not found")
    def get(self, username):
        user_response = requests.get(URL_USERS + f"/{username}")
        if user_response.status_code == 404:
            response = user_response.json(), 404
        else:
            library_models = LibraryModel.find_by_username(username)
            user_books = []
            for libray_model in library_models:
                user_books.append(
                    book_schema.load(requests.get(URL_BOOKS + f"/{libray_model.book_id}").json(),
                                     session=db.session))
            user_object = user_schema.load(user_response.json(), session=db.session)
            user_object.add_books(user_books)
            response = user_schema.dump(user_object), 200

        return response


@library_user_ns.route("/<username>/books/<book_id>")
class IssueBook(Resource):

    @library_user_ns.response(201, "Created", model=library)
    @library_user_ns.response(400, "Bad Request")
    @library_user_ns.response(404, "Not Found")
    def post(self, username, book_id):
        book_response = requests.get(URL_BOOKS + f"/{book_id}")
        user_response = requests.get(URL_USERS + f"/{username}")
        if book_response.status_code == 200 and user_response.status_code == 200:
            library_model = LibraryModel(username, book_id)
            library_model.save_to_db()
            response = library_user_schema.dump(library_model), 201
        else:
            response = book_response.json() | user_response.json(), 404
        return response
