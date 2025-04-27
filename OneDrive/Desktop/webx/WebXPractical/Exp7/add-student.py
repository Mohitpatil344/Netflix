from flask import Flask, request, jsonify
from pymongo import MongoClient
import json
from bson import json_util

app = Flask(__name__)

# Connect to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["school_db"]  # Database name
    students_collection = db["students"]  # Collection name
    print("MongoDB connection successful")
except Exception as e:
    print(f"MongoDB connection error: {e}")

# Parse MongoDB data to JSON
def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.route('/add-student', methods=['POST'])
def add_student():
    try:
        # Get JSON data from request
        student_data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'rollNo', 'department']
        for field in required_fields:
            if field not in student_data:
                return jsonify({
                    "success": False,
                    "error": f"Missing required field: {field}"
                }), 400
        
        # Check if student with same roll number already exists
        existing_student = students_collection.find_one({"rollNo": student_data['rollNo']})
        if existing_student:
            return jsonify({
                "success": False,
                "error": f"Student with roll number {student_data['rollNo']} already exists"
            }), 409
        
        # Insert student into database
        result = students_collection.insert_one(student_data)
        
        # Return success response with inserted student
        inserted_student = students_collection.find_one({"_id": result.inserted_id})
        
        return jsonify({
            "success": True,
            "message": "Student added successfully",
            "student": parse_json(inserted_student)
        }), 201
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# Optional: GET route to view all students (for testing)
@app.route('/students', methods=['GET'])
def get_students():
    try:
        students = list(students_collection.find({}))
        return jsonify({
            "success": True,
            "students": parse_json(students),
            "count": len(students)
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5003)
