from flask import request
from flask_restx import Resource, fields, Namespace
from schemas.book_schema import BookSchema
from models.book_model import BookModel
from db import db

books_ns = Namespace('books', description='Books related operations')
BOOK_NOT_FOUND = "Book not found"
book_schema = BookSchema()
books_schema = BookSchema(many=True)

book = books_ns.model('Book', {
    'name': fields.String('Name of the book'),
    'publisher': fields.String('Name of publisher'),
    'author': fields.String('Name of the author')
})


@books_ns.route('/')
class BooksList(Resource):

    @books_ns.response(200, 'Successful', model=book)
    def get(self):
        return books_schema.dump(BookModel.find_all()), 200

    @books_ns.expect(book)
    @books_ns.response(201, "Created", model=book)
    def post(self):
        book = request.get_json()
        book_data = book_schema.load(book, session=db.session)
        book_data.save_to_db()

        return book_schema.dump(book_data), 201


@books_ns.route('/<book_id>')
class Book(Resource):

    @books_ns.response(200, "Successful", model=book)
    @books_ns.response(404, "Not Found")
    def get(self, book_id):
        book = BookModel.find_by_id(book_id)
        if book:
            response = book_schema.dump(book)
        else:
            response = {'message': BOOK_NOT_FOUND}, 404

        return response
