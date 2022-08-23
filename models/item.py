import json

from database.database import db
from models.order import Order

item_in_order = db.Table('item_in_order',
                         db.Column('item_id', db.Integer, db.ForeignKey('Item.item_id'), primary_key=True),
                         db.Column('order_id', db.Integer, db.ForeignKey('Order.order_id'), primary_key=True)
                         )


class Item(db.Model):
    # __tablename__ = 'Address'

    item_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship('Order', secondary=item_in_order, lazy='subquery',
                             backref=db.backref('Item', lazy=True))

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
