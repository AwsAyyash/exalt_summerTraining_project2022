from flask import request, jsonify
from database.database import db

from restaurant_apis.messages_response import deleted_msg, error_msg

from models.item import Item

from schemas.item_schema import ItemSchema


def get_items():
    """API for returning the items list as json.
        Returns:
            Response: A json response containing the items.
        """

    items_from_db = db.session.query(Item).all()

    item_schema = ItemSchema()
    result = item_schema.dump(items_from_db, many=True)
    return jsonify(result), 200


def post_item():
    """API for returning the item list as json.
        Returns:
            Response: A json dict containing the items.
        """

    item = Item(**request.get_json(force=True))

    db.session.add(item)

    db.session.commit()

    return jsonify({"Item id": item.item_id}), 200


def get_item(item_id):
    """API for returning the item list as json.
        Args:
            item_id (int): The id of the item to return (search for).
        Returns:
            Response: The item of the given item_id (Error if it doesn't exist).
        """

    query_result = db.session.query(Item).filter(Item.item_id == item_id)
    item_schema = ItemSchema()
    result = item_schema.dump(query_result, many=True)

    if len(result) == 0:
        return jsonify(error_msg), 404  # not found

    return jsonify(result[0]), 200


def put_item(item_id):
    """API for returning the item list as dict.
        Args:
            item_id (int): The item_id of the item to return (search for).
        Returns:
            Response: The item of the given item_id (None if it doesn't exist).
        """
    item = Item.query.filter_by(item_id=item_id).first()

    if item is None:
        return jsonify(error_msg), 404  # not found

    request_data = request.get_json(force=True)

    item.name = request_data['name']
    item.description = request_data['description']
    item.price = request_data['price']

    db.session.commit()

    return 200


def delete_item(item_id):
    """API for returning the item list as dict.
        Args:
            item_id (int): The item_id of the item to return (search for).
        Returns:
            Response: The item of the given item_id (None if it doesn't exist).
        """
    deleted = Item.query.filter_by(item_id=item_id).delete()
    db.session.commit()
    if bool(deleted):
        return jsonify(deleted_msg), 200

    return jsonify(error_msg), 404  # not found



