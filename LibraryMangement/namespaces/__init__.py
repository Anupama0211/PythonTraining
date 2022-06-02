from flask_restx import Api
from namespaces.Book_Namespace import books_ns
from namespaces.User_Namespace import users_ns
from namespaces.Library_Book_Namespace import library_book_ns
from namespaces.Library_User_Namespace import library_user_ns

api = Api(title='Library Management API')

api.add_namespace(books_ns)
api.add_namespace(users_ns)
api.add_namespace(library_book_ns)
api.add_namespace(library_user_ns)
