from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.item import Item


class ItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        include_fk = True
        load_instance = True
