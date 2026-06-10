from flask import Blueprint, request, jsonify
from services.task_service import add_task_service, fetch_tasks_service

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    add_task_service(
        data["title"],
        data["description"],
        data["priority"],
        data["user_id"]
    )
    return jsonify({"message": "Task created"})

@task_bp.route("/tasks/<int:user_id>", methods=["GET"])
def get_tasks(user_id):
    tasks = fetch_tasks_service(user_id)
    result = []
    for t in tasks:
        result.append({
            "id": t["id"],
            "title": t["title"],
            "status": t["status"],
            "priority": t["priority"]
        })
    return jsonify(result)