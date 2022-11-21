import json as json

from database.database import db
from models.employee import Employee

import models.item


class Chef(Employee):
    __tablename__ = 'Chef'
    experience = db.Column(db.Integer, nullable=False)

    items = db.relationship("Item", backref=db.backref('Chef'))

    def add_item(self, item: models.item.Item):
        self.items.append(item)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
