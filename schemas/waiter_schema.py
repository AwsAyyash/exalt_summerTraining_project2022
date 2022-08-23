from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.waiter import Waiter


class WaiterSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Waiter
        include_fk = True
        load_instance = True
