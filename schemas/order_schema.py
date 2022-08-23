from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.order import Order


class OrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        include_fk = True
        load_instance = True
