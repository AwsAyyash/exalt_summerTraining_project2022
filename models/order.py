import json

from database.database import db
from sqlalchemy.sql import func

# import models.item as itm
# print("line35_Order class")
# from models.item import Item
from models.waiter import Waiter
from models.customer import Customer

# from models.item import Item

item_in_order = db.Table('item_in_order',
                         db.Column('item_id', db.Integer, db.ForeignKey('Item.item_id'), primary_key=True),
                         db.Column('order_id', db.Integer, db.ForeignKey('Order.order_id'), primary_key=True)
                         )


class Order(db.Model):
    __tablename__ = 'Order'

    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
    cost = db.Column(db.Float, nullable=True)

    date_ordered = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    #
    waiter_id = db.Column(db.Integer, db.ForeignKey('Waiter.employee_id'), nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('Customer.customer_id'), nullable=True)
    print("line26_Order class")
    items = db.relationship('Item', secondary=item_in_order,backref='Order')


    def add_item(self, item):
        self.items.append(item)

    def set_items(self, items):
        self.items = items

    def add_to_cost(self, amount_to_be_added: float):
        self.cost = float(self.cost) + float(amount_to_be_added)

    def remove_items(self):
        self.items = []
        self.cost = 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
