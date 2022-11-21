from ma import ma
from models.Item import ItemModel



class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemModel
        load_instance = True
        load_only = ("store",)
        include_fk= True