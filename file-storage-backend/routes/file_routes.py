import os
from flask import Blueprint, request, jsonify, send_from_directory, render_template
from database import get_db
from services.file_service import save_file
from config import UPLOAD_FOLDER

file_bp = Blueprint("file_bp", __name__)

@file_bp.route("/api/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file"}), 400
    
    file = request.files["file"]
    result = save_file(file)
    
    if not result:
        return jsonify({"error": "Invalid file"}), 400
    
    filename, filepath = result
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO files (filename, filepath) VALUES (?, ?)", (filename, filepath))
    conn.commit()
    conn.close()
    return jsonify({"message": "Uploaded successfully"})

@file_bp.route("/api/files", methods=["GET"])
def get_files():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM files")
    files = cursor.fetchall()
    conn.close()
    return jsonify([dict(f) for f in files])

@file_bp.route("/api/downloads/<filename>", methods=["GET"])
def download(filename):
    return send_from_directory(
        UPLOAD_FOLDER,
        filename,
        as_attachment=True
    )

@file_bp.route("/api/delete/<int:file_id>", methods=["DELETE"])
def delete(file_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT filepath FROM files WHERE id=?", (file_id,))
    file = cursor.fetchone()

    if not file:
        return jsonify({"error": "Not found"}), 404
    
    filepath = file["filepath"]
    cursor.execute("DELETE FROM files WHERE id=?", (file_id,))
    conn.commit()
    conn.close()

    if os.path.exists(filepath):
        os.remove(filepath)
    
    return jsonify({"message": "Deleted"})