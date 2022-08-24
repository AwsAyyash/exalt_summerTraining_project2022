from flask import request, jsonify
from database.database import db

from restaurant_apis.messages_response import deleted_msg, error_msg

from models.customer import Customer

from schemas.customer_schema import CustomerSchema


def get_customers():
    """API for returning the customers list as json.
        Returns:
            Response: A json response containing the customers.
        """

    customers_from_db = db.session.query(Customer).all()

    customer_schema = CustomerSchema()
    result = customer_schema.dump(customers_from_db, many=True)
    return jsonify(result), 200


def post_customer():
    """API for returning the customer list as json.
        Returns:
            Response: A json dict containing the customers.
        """

    customer = Customer(**request.get_json(force=True))

    db.session.add(customer)

    db.session.commit()

    return jsonify({"Customer id": customer.customer_id}), 200


def get_customer(customer_id):
    """API for returning the customer list as json.
        Args:
            customer_id (int): The id of the customer to return (search for).
        Returns:
            Response: The customer of the given customer_id (Error if it doesn't exist).
        """

    query_result = db.session.query(Customer).filter(Customer.customer_id == customer_id)
    customer_schema = CustomerSchema()
    result = customer_schema.dump(query_result, many=True)

    if len(result) == 0:
        return jsonify(error_msg), 404  # not found

    return jsonify(result[0]), 200


def put_customer(customer_id):
    """API for returning the user list as dict.
        Args:
            customer_id (int): The user_id of the user to return (search for).
        Returns:
            Response: The user of the given user_id (None if it doesn't exist).
        """
    customer = Customer.query.filter_by(customer_id=customer_id).first()

    if customer is None:
        return jsonify(error_msg), 404  # not found

    request_data = request.get_json(force=True)

    customer.first_name = request_data['first_name']
    customer.last_name = request_data['last_name']
    customer.user_name = request_data['user_name']
    customer.email = request_data['email']

    db.session.commit()

    return 200


def delete_customer(customer_id):
    """API for returning the user list as dict.
        Args:
            customer_id (int): The user_id of the user to return (search for).
        Returns:
            Response: The user of the given user_id (None if it doesn't exist).
        """
    deleted = Customer.query.filter_by(customer_id=customer_id).delete()
    db.session.commit()
    if bool(deleted):
        return jsonify(deleted_msg), 200

    return jsonify(error_msg), 404  # not found



