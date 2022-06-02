from flask_restx import Api
from namespaces.Book_Namespace import books_ns
from namespaces.User_Namespace import users_ns

api=Api(title='Library Management API')

api.add_namespace(books_ns)
api.add_namespace(users_ns)