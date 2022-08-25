from flask import request, jsonify
from database.database import db
from models.item import Item

from restaurant_apis.messages_response import deleted_msg, error_msg

from models.order import Order, item_in_order

from schemas.order_schema import OrderSchema


def get_orders():
    """API for returning the orders list as json.
        Returns:
            Response: A json response containing the orders.
        """

    orders_from_db = db.session.query(Order).all()

    order_schema = OrderSchema()
    result = order_schema.dump(orders_from_db, many=True)
    return jsonify(result), 200


def post_order():
    """API for returning the order list as json.
        Returns:
            Response: A json dict containing the orders.
        """
    items_for_this_order_in_request_body = request.get_json(force=True)['items'] # is an array of items IDs

    order = Order()
    order.cost = 0.0
    db.session.add(order)
    db.session.commit()

    #print(f'id orde ---- order.order_id==== {order.order_id}')
    order = Order.query.filter_by(order_id=order.order_id).first()

    #items = []
    #total_cost = 0.0
    for item_id in items_for_this_order_in_request_body:  # phone: is a dict
        #with db.session.no_autoflush:
        item = Item.query.filter_by(item_id=item_id).first()
     #   print(f'inside orders_api_L38: item= {item.name}')
        if item is not None:
            order.items.append(item)
            order.add_to_cost(float(item.price))
        #total_cost += item.price
        #order.add_item(item)
        #order.add_to_cost(item.price)

    #order = Order(items = items, cost= total_cost)
    #db.session.add(order)
    #print(f'order: inside orders_api: L46= {order.order_id},  {order.date_ordered}, {order.cost}, items= {order.items}')

    db.session.commit()
    #print(f'order: inside orders_api: L49= {order.order_id},  {order.date_ordered}, {order.cost}, items= {order.items}')

    print(f'-------------------------------')

    #multy_many_from_db = db.session.query(item_in_order).all()

    #print(f'multy_many_from_db={multy_many_from_db}')

    #print(f'-------------------------------')

    return jsonify({"Order id": order.order_id}), 200


def get_order(order_id):
    """API for returning the order list as json.
        Args:
            order_id (int): The id of the order to return (search for).
        Returns:
            Response: The order of the given order_id (Error if it doesn't exist).
        """

    query_result = db.session.query(Order).filter(Order.order_id == order_id)
    order_schema = OrderSchema()
    result = order_schema.dump(query_result, many=True)

    if len(result) == 0:
        return jsonify(error_msg), 404  # not found

    return jsonify(result[0]), 200


def put_order(order_id):
    """API for returning the order list as dict.
        Args:
            order_id (int): The order_id of the order to return (search for).
        Returns:
            Response: The order of the given order_id (None if it doesn't exist).
        """

    items_for_this_order_in_request_body = request.get_json(force=True)['items'] # is an array of items IDs

    order = Order.query.filter_by(order_id=order_id).first()
    order.remove_items()
    for item_id in items_for_this_order_in_request_body:  # phone: is a dict

        item = Item.query.filter_by(item_id=item_id).first()

        if item is not None:
            order.add_item(item)
            order.add_to_cost(item.price)

    db.session.commit()

    return 200


def delete_order(order_id):
    """API for returning the order list as dict.
        Args:
            order_id (int): The order_id of the order to return (search for).
        Returns:
            Response: The order of the given order_id (None if it doesn't exist).
        """
    deleted = Order.query.filter_by(order_id=order_id).delete()
    db.session.commit()
    if bool(deleted):
        return jsonify(deleted_msg), 200

    return jsonify(error_msg), 404  # not found
