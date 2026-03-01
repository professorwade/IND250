from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CONFIGURATION: Tells Flask where to store the SQLite database file
# 'sqlite:///tasks.db' creates a file named tasks.db in your project folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# DATA MODEL: Defines what a "Task" looks like in our database
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Unique ID for each task
    title = db.Column(db.String(100), nullable=False) # The task text

# INITIALIZATION: Creates the database file and table if they don't exist
with app.app_context():
    db.create_all()

# --- ROUTES ---

# HOME: Serves the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# CREATE: Receives JSON data and saves a new task to the DB
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json() # Get the data sent from JavaScript
    new_task = Task(title=data['title']) # Create a new Task object
    db.session.add(new_task) # Stage the task
    db.session.commit()      # Save to the .db file
    return jsonify({"message": "Task created!"}), 201

# READ: Fetches all tasks from the DB and returns them as a List of JSON
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all() # Fetch every row in the Task table
    # Convert Python objects into a format JavaScript understands (JSON)
    output = [{"id": t.id, "title": t.title} for t in tasks]
    return jsonify(output)

# UPDATE: Finds a specific task by ID and changes its title
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id) # Find task or return 404 error
    data = request.get_json()
    task.title = data['title'] # Update the title
    db.session.commit()        # Save changes
    return jsonify({"message": "Task updated!"})

# DELETE: Removes a task from the database
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task) # Mark for deletion
    db.session.commit()     # Apply deletion
    return jsonify({"message": "Task deleted!"})

if __name__ == '__main__':
    app.run(debug=True) # Run in debug mode for easy development