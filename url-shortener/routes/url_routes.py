from flask import Blueprint, request, jsonify, redirect
from utils.jwt_handler import verify_token
from models.url_model import get_url, increase_clicks
from services.url_service import create_short_url

url_bp = Blueprint("url", __name__)

def auth_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        user_id = verify_token(token)
        if not user_id:
            return jsonify({"error": "Unauthorized"}), 401
        return func(user_id, *args, **kwargs)
    return wrapper

@url_bp.route("/shorten", methods=["POST"])
@auth_required
def shorten(user_id):
    data = request.json
    code = create_short_url(data["url"], user_id)
    return jsonify({
        "short_url": f"http://127.0.0.1:5000/{code}"
    })

@url_bp.route("/<short_code>")
def redirect_url(short_code):
    data = get_url(short_code)
    if data:
        increase_clicks(short_code)
        return redirect(data["original_url"])
    return jsonify({"error": "Invalid URL"}), 404