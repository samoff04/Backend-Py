from flask import Flask, request, jsonify
app = Flask(__name__)
tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    task = {
        "id": len(tasks) + 1,
        "task": data["task"],
        "done": False
    }
    tasks.append(task)
    return jsonify({"message": "Task added", "task": task})

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json
    for task in tasks:
        if task["id"] == task_id:
            task["task"] = data.get("task", task["task"])
            task["done"] = data.get("done", task["done"])
            return jsonify({"message": "Task updated", "task": task})
    return jsonify({"message": "Task not found"})

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted"})
    return jsonify({"message": "Task not found"})

if __name__ == "__main__":
    app.run(debug=True)