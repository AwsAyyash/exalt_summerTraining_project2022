from flask import request, jsonify
from database.database import db
from models.item import Item

from restaurant_apis.messages_response import deleted_msg, error_msg

from models.chef import Chef

from schemas.chef_schema import ChefSchema


def get_chefs():
    """API for returning the chefs list as json.
        Returns:
            Response: A json response containing the chefs.
        """

    chefs_from_db = db.session.query(Chef).all()

    chef_schema = ChefSchema()
    result = chef_schema.dump(chefs_from_db, many=True)
    print(f'result={type(result)}:{result}')
    return jsonify(result), 200


def post_chef():
    """API for returning the chef list as json.
        Returns:
            Response: A json dict containing the chefs.
        """

    chef = Chef(**request.get_json(force=True), employee_type='chef')

    db.session.add(chef)

    db.session.commit()

    return jsonify({"Chef id": chef.employee_id}), 200


def get_chef(employee_id):
    """API for returning the chef list as json.
        Args:
            employee_id (int): The id of the chef to return (search for).
        Returns:
            Response: The chef of the given chef_id (Error if it doesn't exist).
        """

    query_result = db.session.query(Chef).filter(Chef.employee_id == employee_id)
    chef_schema = ChefSchema()
    result = chef_schema.dump(query_result, many=True)

    if len(result) == 0:
        return jsonify(error_msg), 404  # not found

    return jsonify(result[0]), 200


def put_chef(employee_id):
    """API for returning the user list as dict.
        Args:
            employee_id (int): The user_id of the user to return (search for).
        Returns:
            Response: The user of the given user_id (None if it doesn't exist).
        """
    chef = Chef.query.filter_by(employee_id=employee_id).first()

    if chef is None:
        return jsonify(error_msg), 404  # not found

    request_data = request.get_json(force=True)

    chef.first_name = request_data['first_name']
    chef.last_name = request_data['last_name']
    chef.experience = request_data['experience']
    chef.national_id = request_data['national_id']

    chef.email = request_data['email']
    chef.daily_working_hours = request_data['daily_working_hours']
    chef.hour_wage = request_data['hour_wage']

    db.session.commit()

    return 200


def delete_chef(employee_id):
    """API for returning the user list as dict.
        Args:
            employee_id (int): The user_id of the user to return (search for).
        Returns:
            Response: The user of the given user_id (None if it doesn't exist).
        """
    deleted = Chef.query.filter_by(employee_id=employee_id).delete()
    db.session.commit()
    if bool(deleted):
        return jsonify(deleted_msg), 200

    return jsonify(error_msg), 404  # not found


def post_item_to_chef(employee_id):
    item_id = int(request.data)
    chef = Chef.query.filter_by(employee_id=employee_id).first()
    item = Item.query.filter_by(item_id=item_id).first()
    item.chef_id = chef.employee_id
    chef.add_item(item)
    db.session.commit()
    return 200


def add_item_to_chef(): # ask if needed
    pass
