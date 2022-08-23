from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.address import Address


class AddressSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        include_fk = True
        load_instance = True
