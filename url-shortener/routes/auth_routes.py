from flask import Blueprint, request, jsonify
from services.auth_service import register_user, login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    register_user(data["username"], data["password"])
    return jsonify({"message": "User created"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    token = login_user(data["username"], data["password"])
    if token:
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401