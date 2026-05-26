from flask import Blueprint, request, jsonify
from models.post_model import *

post_bp = Blueprint("post_bp", __name__)

@post_bp.route("/posts", methods=["POST"])
def add_post():
    data = request.json
    create_post(data["title"], data["content"])
    return jsonify({"message": "Post created"})

@post_bp.route("/posts", methods=["GET"])
def get_all_posts():
    rows = get_posts()
    posts=[]
    for row in rows:
        posts.append({"id": row["id"],
                      "title": row["title"],
                      "content": row["content"],
                      "created_at": row["created_at"]
                      })
    return jsonify(posts)

@post_bp.route("/posts/<int:id>", methods=["PUT"])
def edit_post(id):
    data = request.json
    update_post(id, data["title"], data["content"])
    return jsonify({"message": "Post updated"})

@post_bp.route("/posts/<int:id>", methods=["DELETE"])
def remove_post(id):
    delete_post(id)
    return jsonify({"message": "Post deleted"})