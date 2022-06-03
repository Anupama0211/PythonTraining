from ma import ma
from models.user_model import UserModel
from schemas.book_schema import BookSchema


class UserSchema(ma.SQLAlchemyAutoSchema):
    books = ma.Nested(BookSchema, many=True)

    class Meta:
        model = UserModel
        load_instance = True
