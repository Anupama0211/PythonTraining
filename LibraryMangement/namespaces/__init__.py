from flask_restx import Api
from namespaces.book_namespace import books_ns
from namespaces.user_namespace import users_ns
from namespaces.library_book_namespace import library_book_ns
from namespaces.library_user_namespace import library_user_ns

api = Api(title='Library Management API')

api.add_namespace(books_ns)
api.add_namespace(users_ns)
api.add_namespace(library_book_ns)
api.add_namespace(library_user_ns)
