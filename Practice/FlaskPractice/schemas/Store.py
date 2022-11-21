from ma import ma
from models.Store import StoreModel
from models.Item import ItemModel
from schemas.Item import ItemSchema


class StoreSchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(ItemSchema, many=True)

    class Meta:
        model = StoreModel
        load_instance = True
        include_fk = True