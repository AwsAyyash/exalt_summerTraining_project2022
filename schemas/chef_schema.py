from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.chef import Chef
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from schemas.item_schema import ItemSchema


class ChefSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Chef
        include_fk = True
        load_instance = True
    items = Nested(ItemSchema(only=('name', 'description', 'price')), many=True)
