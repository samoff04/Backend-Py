from flask import Blueprint, request, jsonify
from models.product_model import *

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/products", methods=["POST"])
def create_product():
    data = request.json
    add_product(
        data["name"],
        data["price"]
    )
    return jsonify({"message": "Product added"})

@product_bp.route("/products", methods=["GET"])
def products():
    rows = get_products()
    result = []
    for row in rows:
        result.append({
            "id": row["id"],
            "name": row["name"],
            "price": row["price"]
        })
    return jsonify(result)