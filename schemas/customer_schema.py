from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from models.customer import Customer
from schemas.order_schema import OrderSchema


class CustomerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        include_fk = True
        load_instance = True

    orders = Nested(OrderSchema(only=('cost', 'date_ordered', 'items')), many=True)
