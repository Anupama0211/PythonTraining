from flask import request
from flask_restx import Resource, fields, Namespace, abort
from schemas.user_schema import UserSchema
from models.user_model import UserModel
from db import db

users_ns = Namespace('users', description="User Related operations")

users_schema = UserSchema(many=True)
user_schema = UserSchema()

USER_NOT_FOUND = "User not found"

user = users_ns.model('User', {
    'username': fields.String("UserName", min_length=5),
    'name': fields.String("Name"),
    'email': fields.String("Email"),
    'books': fields.Raw("Books", required=False)
})


@users_ns.route('/')
class UserList(Resource):

    @users_ns.response(200, "Successful", model=[user])
    def get(self):
        return users_schema.dump(UserModel.find_all()), 200

    @users_ns.expect(user, validate=True)
    @users_ns.response(201, "Created", model=user)
    @users_ns.response(400, "Bad Request")
    def post(self):
        user_json = request.get_json()
        user_object = user_schema.load(user_json, session=db.session)
        user_object.save_to_db()
        return user_schema.dump(user_object), 201


@users_ns.route('/<username>')
class User(Resource):

    @users_ns.response(200, "Successful", model=user)
    @users_ns.response(404, "Not found")
    def get(self, username):
        user = UserModel.find_by_username(username)
        if user:
            return user_schema.dump(user)
        abort(404, USER_NOT_FOUND)
