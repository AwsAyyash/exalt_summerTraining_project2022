import json as json

from database.database import db
from models.employee import Employee

from models.item import Item


class Chef(Employee):
    experience = db.Column(db.Integer, nullable=False)

    items = db.relationship("Item", backref=db.backref('Chef', lazy=True), uselist=True, cascade='all,delete')

    def add_item(self, item: Item):
        self.items.append(item)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
