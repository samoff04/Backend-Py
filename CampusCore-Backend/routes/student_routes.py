from flask import Blueprint, request, jsonify
from models.student_model import *

student_bp = Blueprint("student_bp", __name__)

@student_bp.route("/students", methods=["POST"])
def create_student():
    data = request.json
    add_student(data["name"], data["age"], data["course"])
    return jsonify({"message": "Student added"})

@student_bp.route("/students", methods=["GET"])
def get_students():
    rows = get_all_students()
    students = []
    for row in rows:
        students.append({
            "id": row["id"],
            "name": row["name"],
            "age": row["age"],
            "course": row["course"]
        })
    return jsonify(students)

@student_bp.route("/students/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    update_student(id, data["name"], data["age"], data["course"])
    return jsonify({"message": "Student updated"})