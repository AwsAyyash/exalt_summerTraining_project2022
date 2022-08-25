import json

from database.database import db

#import models

class Item(db.Model):
    __tablename__ = 'Item'

    item_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    #orders = db.Column(db.Integer, db.ForeignKey('Order.order_id'),  nullable=True)
    chef_id = db.Column(db.Integer, db.ForeignKey('Chef.employee_id'), nullable=True)


    #def add_order(self,order):
     #   self.orders.append(order)
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    from models.order import Order
