from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from models.order import Order
from schemas.item_schema import ItemSchema


class OrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        include_fk = True
        load_instance = True

    items = Nested(ItemSchema(only=('name', 'description', 'price')), many=True)

