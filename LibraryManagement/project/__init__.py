from flask import Flask
from flask_restx import Api
from marshmallow import ValidationError

from exceptions.invalid_operation_exception import InvalidOperationException
from namespaces.book_namespace import books_ns
from namespaces.library_book_namespace import library_book_ns
from namespaces.library_user_namespace import library_user_ns
from namespaces.user_namespace import users_ns
from project.db import db
from project.ma import ma
from project.middleware import init_middlewares


def create_app():
    api = Api(title='Library Management API')
    api.add_namespace(books_ns)
    api.add_namespace(users_ns)
    api.add_namespace(library_book_ns)
    api.add_namespace(library_user_ns)

    app = Flask(__name__)

    USERNAME = "root"
    PASSWORD = "abcdef"
    SERVER = "localhost:3306"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{SERVER}/library_management'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True

    init_middlewares(app)
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)

    @api.errorhandler(ValidationError)
    def handle_validation_error(error):
        return {'message': error}, 400

    @api.errorhandler(InvalidOperationException)
    def handle_validation_error(error):
        return {'message': error.message}, 400

    return app
