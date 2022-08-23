from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.customer import Customer


class CustomerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        include_fk = True
        load_instance = True
