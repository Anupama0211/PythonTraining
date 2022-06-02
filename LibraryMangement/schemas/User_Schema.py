from marshmallow import Schema, fields
from models.User_Model import UserModel


class UserSchema(Schema):
    class Meta:
        model = UserModel
        load_instance = True
