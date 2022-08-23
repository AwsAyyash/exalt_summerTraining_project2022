import json

from database.database import db
from models.order import Order


class Customer(db.Model):
    # __tablename__ = 'Address'

    customer_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    orders = db.relationship("Order", backref=db.backref('Customer', lazy=True), uselist=True, cascade='all,delete')

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
