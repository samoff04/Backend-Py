from flask import Blueprint, jsonify
from services.order_service import checkout

order_bp = Blueprint("order_bp", __name__)

@order_bp.route("/checkout", methods=["POST"])
def order_checkout():
    total = checkout()
    return jsonify({
        "message": "Order placed",
        "total": total
    })