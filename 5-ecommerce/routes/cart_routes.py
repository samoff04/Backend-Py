from flask import Blueprint, request, jsonify
from models.cart_model import *

cart_bp = Blueprint("cart_bp", __name__)

@cart_bp.route("/cart", methods=["POST"])
def cart_add():
    data = request.json
    add_to_cart(
        data["product_id"],
        data["quantity"]
    )
    return jsonify({"message": "Added to cart"})

@cart_bp.route("/cart", methods=["GET"])
def cart_items():
    rows = get_cart()
    result = []
    for row in rows:
        result.append({
            "product_id": row["product_id"],
            "quantity": row["quantity"]
        })
    return jsonify(result)