import json

from database.database import db

from models.employee import Employee
from models.order import Order


class Waiter(Employee):
    orders = db.relationship("Order", backref=db.backref('Waiter', lazy=True), uselist=True, cascade='all,delete')

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
