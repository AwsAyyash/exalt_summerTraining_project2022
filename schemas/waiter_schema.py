from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.waiter import Waiter
from marshmallow_sqlalchemy.fields import Nested

from schemas.order_schema import OrderSchema


class WaiterSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Waiter
        include_fk = True
        load_instance = True
    orders = Nested(OrderSchema(only=('cost', 'date_ordered', 'items')), many=True)
