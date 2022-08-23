from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.chef import Chef


class ChefSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Chef
        include_fk = True
        load_instance = True
