from ma import ma
from models.Book_Model import BookModel


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel
        load_instance = True
