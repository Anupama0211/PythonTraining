from flask import request
from flask_restx import Resource,Namespace
from namespaces.Book_Namespace import book
import requests

library_book_ns = Namespace("library/books", description="Library book related operations")


@library_book_ns.route("/")
class Library_Books(Resource):
    def get(self):
        return requests.get("http://127.0.0.1:5000/books").json()

    @library_book_ns.expect(book)
    def post(self):
        book_json = request.get_json()
        return requests.post("http://127.0.0.1:5000/books", json=book_json).json(), 201

@library_book_ns.route("/<id>")
class Library_Book(Resource):
    def get(self,id):
        return requests.get(f"http://127.0.0.1:5000/books/{id}").json()