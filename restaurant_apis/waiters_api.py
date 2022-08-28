from flask import request, jsonify
from database.database import db
from models.order import Order

from restaurant_apis.messages_response import deleted_msg, error_msg

from models.waiter import Waiter

from schemas.waiter_schema import WaiterSchema


def get_waiters():
    """API for returning the waiters list as json.
        Returns:
            Response: A json response containing the waiters.
        """

    waiters_from_db = db.session.query(Waiter).all()

    waiter_schema = WaiterSchema()
    result = waiter_schema.dump(waiters_from_db, many=True)
    return jsonify(result), 200


def post_waiter():
    """API for returning the waiter list as json.
        Returns:
            Response: A json dict containing the waiters.
        """

    waiter = Waiter(**request.get_json(force=True), employee_type='waiter')

    db.session.add(waiter)

    db.session.commit()

    return jsonify({"Waiter id": waiter.employee_id}), 200


def get_waiter(employee_id):
    """API for returning the waiter list as json.
        Args:
            employee_id (int): The id of the waiter to return (search for).
        Returns:
            Response: The waiter of the given waiter_id (Error if it doesn't exist).
        """

    query_result = db.session.query(Waiter).filter(Waiter.employee_id == employee_id)
    waiter_schema = WaiterSchema()
    result = waiter_schema.dump(query_result, many=True)

    if len(result) == 0:
        return jsonify(error_msg), 404  # not found

    return jsonify(result[0]), 200


def put_waiter(employee_id):
    """API for returning the user list as dict.
        Args:
            employee_id (int): The user_id of the user to return (search for).
        Returns:
            Response: The user of the given user_id (None if it doesn't exist).
        """
    waiter = Waiter.query.filter_by(employee_id=employee_id).first()

    if waiter is None:
        return jsonify(error_msg), 404  # not found

    request_data = request.get_json(force=True)

    waiter.first_name = request_data['first_name']
    waiter.last_name = request_data['last_name']
    waiter.national_id = request_data['national_id']

    waiter.email = request_data['email']
    waiter.daily_working_hours = request_data['daily_working_hours']
    waiter.hour_wage = request_data['hour_wage']

    db.session.commit()

    return 200


def delete_waiter(employee_id):
    """API for returning the user list as dict.
        Args:
            employee_id (int): The user_id of the user to return (search for).
        Returns:
            Response: The user of the given user_id (None if it doesn't exist).
        """
    deleted = Waiter.query.filter_by(employee_id=employee_id).delete()
    db.session.commit()
    if bool(deleted):
        return jsonify(deleted_msg), 200

    return jsonify(error_msg), 404  # not found


def post_for_waiter_prepare_order(employee_id):
    order_id = int(request.data)
    waiter = Waiter.query.filter_by(employee_id=employee_id).first()
    order = Order.query.filter_by(order_id=order_id).first()
    order.waiter_id = waiter.employee_id
    waiter.add_order(order)
    db.session.commit()
    return 200
