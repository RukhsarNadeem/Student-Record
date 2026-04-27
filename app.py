from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'student_data.json'

# Initialize JSON file if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()

    new_student = {
        "name": data['name'],
        "department": data['department'],
        "roll_number": data['roll_number']
    }

    with open(DATA_FILE, 'r') as f:
        students = json.load(f)

    students.append(new_student)

    with open(DATA_FILE, 'w') as f:
        json.dump(students, f, indent=4)

    return jsonify({"message": "Student added successfully!"})

@app.route('/get_students')
def get_students():
    with open(DATA_FILE, 'r') as f:
        students = json.load(f)
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)