from flask import request
from flask_restx import Resource, fields, Namespace
from schemas.Book_Schema import BookSchema
from models.Book_Model import BookModel
from db import db

books_ns = Namespace('books', description='Books related operations')
BOOK_NOT_FOUND = "Book not found"
book_schema = BookSchema()
books_schema = BookSchema(many=True)

book = books_ns.model('Book', {
    'id': fields.Integer,
    'name': fields.String('Name of the book'),
    'publisher': fields.String('Name of publisher'),
    'author': fields.String('Name of the author')
})


@books_ns.route('/<id>')
class Book(Resource):

    @books_ns.response(200, "Successful", model=book)
    def get(self, id):
        book_data = BookModel.find_by_id(id)
        if book_data:
            response = book_schema.dump(book_data)
        else:
            response = {'message': BOOK_NOT_FOUND}, 404
        return response


@books_ns.route('/')
class BooksList(Resource):

    @books_ns.response(200, 'Successful', model=book)
    def get(self):
        return books_schema.dump(BookModel.find_all()), 200

    @books_ns.expect(book)
    @books_ns.response(201, "Created", model=book)
    def post(self):
        book_json = request.get_json()
        book_data = book_schema.load(book_json, session=db.session)
        response = book_schema.dump(book_data), 201
        book_data.save_to_db()

        return response
