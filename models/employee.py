import json

from database.database import db


class Employee(db.Model):
    # __tablename__ = 'Address'
    __abstract__ = True

    employee_id = db.Column(db.Integer, primary_key=True, nullable=False)
    employee_type = db.Column(db.String(100), nullable=False) # chef, waiter
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    national_id = db.Column(db.Integer, nullable=False)
    daily_working_hours = db.Column(db.Integer, nullable=False)
    hour_wage = db.Column(db.Float, nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
