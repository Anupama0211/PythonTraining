import requests
from flask import request
from flask_restx import Resource, Namespace
from namespaces.book_namespace import book

library_book_ns = Namespace("library/books", description="Library book related operations")

URL = "http://127.0.0.1:5001/books"


@library_book_ns.route("/")
class LibraryBooks(Resource):

    @library_book_ns.response(200, "Successful", model=[book])
    def get(self):
        response = requests.get(URL)
        return response.json(), response.status_code

    @library_book_ns.expect(book, validate=True)
    @library_book_ns.response(201, "Created", model=book)
    def post(self):
        book_json = request.get_json()
        return requests.post(URL, json=book_json).json(), 201


@library_book_ns.route("/<book_id>")
class LibraryBook(Resource):

    @library_book_ns.response(200, "Successful", model=book)
    @library_book_ns.response(404, "Not Found")
    def get(self, book_id):
        response = requests.get(URL + f"/{book_id}")
        return response.json(), response.status_code
