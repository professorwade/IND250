import json
import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# The path to our JSON file
DATA_FILE = 'tasks.json'


# HELPER FUNCTION: Read data from the JSON file
def load_tasks():
    # If the file doesn't exist, return an empty list
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


# HELPER FUNCTION: Write data to the JSON file
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)


# --- ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')


# CREATE: Add a new task to the JSON list
@app.route('/tasks', methods=['POST'])
def add_task():
    tasks = load_tasks()
    data = request.get_json()

    # Create a new task object with a unique ID (timestamp or length-based)
    new_task = {
        "id": len(tasks) + 1 if tasks else 1,
        "title": data['title']
    }

    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task), 201


# READ: Return the full list from the JSON file
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)


# UPDATE: Find the task by ID in the list and change it
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tasks = load_tasks()
    data = request.get_json()

    # Find the task in the list
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = data['title']
            save_tasks(tasks)
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404


# DELETE: Filter out the task with the matching ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    # Keep every task EXCEPT the one we want to delete
    updated_tasks = [t for t in tasks if t['id'] != task_id]

    if len(tasks) == len(updated_tasks):
        return jsonify({"error": "Task not found"}), 404

    save_tasks(updated_tasks)
    return jsonify({"message": "Deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)