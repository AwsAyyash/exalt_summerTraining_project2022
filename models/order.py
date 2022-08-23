import json

from database.database import db
from models.item import Item
from models.waiter import Waiter
from models.customer import Customer


class Order(db.Model):
    # __tablename__ = 'Address'

    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
    cost = db.Column(db.Float, nullable=False)

    date_ordered = db.Column(db.DateTime, nullable=False)
    items = db.Column(db.Integer, db.ForeignKey('Item.item_id'), uselist=True, nullable=False)
    waiter_id = db.Column(db.Integer, db.ForeignKey('Waiter.employee_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('Customer.customer_id'), nullable=False)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
