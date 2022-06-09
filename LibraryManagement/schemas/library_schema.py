from project.ma import ma
from models.library_model import LibraryModel


class LibrarySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LibraryModel
        load_instance = True
