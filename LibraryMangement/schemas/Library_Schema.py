from ma import ma
from models.Library_Model import LibraryModel


class LibrarySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LibraryModel
        load_instance = True
