from ma import ma
from models.User_Model import UserModel
from schemas.Book_Schema import BookSchema


class UserSchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(BookSchema, many=True)

    class Meta:
        model = UserModel
        load_instance = True
