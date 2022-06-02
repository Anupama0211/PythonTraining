from flask import request
from flask_restx import Resource, fields, Namespace
from schemas.User_Schema import UserSchema
from models.User_Model import UserModel
from db import db

users_ns = Namespace('users', description="User Related operations")

users_schema = UserSchema(many=True)
user_schema = UserSchema()

USER_NOT_FOUND = "User not found"

user = users_ns.model('User', {
    'username': fields.String("UserName"),
    'name': fields.String("Name"),
    'email': fields.String("Email")
})


@users_ns.route('/<username>')
class User(Resource):
    @users_ns.response(200, "Succesful", model=user)
    def get(self, username):
        user_data = UserModel.find_by_username(username)
        if user_data:
            response = user_schema.dump(user_data)
        else:
            response = {'message': USER_NOT_FOUND}, 404
        return response


@users_ns.route('/')
class UserList(Resource):
    @users_ns.response(200, "Successful", model=user)
    def get(self):
        return user_schema.dump(UserModel.find_all()), 200

    @users_ns.expect(user)
    @users_ns.response(201, "Created", model=user)
    def post(self):
        user_json = request.get_json()
        user_data = user_schema.load(user_json, session=db.session)
        response = user_schema.dump(user_data), 201
        user_data.save_to_db()

        return response
