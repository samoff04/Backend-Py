from flask import Blueprint, request, jsonify
from services.auth_service import *

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    register_user(data["username"], data["password"])
    return jsonify({"message": "User registered"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    success = login_user(data["username"], data["password"])
    if success:
        return jsonify({"message": "Login success"})
    return jsonify({"message": "Invalid credentials"}), 401