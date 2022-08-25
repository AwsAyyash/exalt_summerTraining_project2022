import json

from database.database import db

from models.employee import Employee

import models
class Waiter(Employee):
    __tablename__ = 'Waiter'
    orders = db.relationship("Order", backref=db.backref('Waiter', lazy=True))

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

