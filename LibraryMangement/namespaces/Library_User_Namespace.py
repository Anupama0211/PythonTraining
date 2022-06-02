from flask import request
from flask_restx import Resource,Namespace
from namespaces.User_Namespace import user
import requests

library_user_ns = Namespace("library/user", description="Library user related operations")

@library_user_ns.route("/")
class Library_Users(Resource):
    def get(self):
        return requests.get("http://127.0.0.1:5000/users").json()

    @library_user_ns.expect(user)
    def post(self):
        user_json = request.get_json()
        return requests.post("http://127.0.0.1:5000/users", json=user_json).json(), 201

@library_user_ns.route("/<username>")
class Library_User(Resource):
    def get(self,username):
        return requests.get(f"http://127.0.0.1:5000/users/{username}").json()