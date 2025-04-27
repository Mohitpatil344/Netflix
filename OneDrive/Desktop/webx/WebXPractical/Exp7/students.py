from flask import Flask, jsonify
from pymongo import MongoClient
import json
from bson import json_util

app = Flask(__name__)

# Connect to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["school_db"]  # Database name
    students_collection = db["students"]  # Collection name
    
    # Insert sample data if collection is empty
    if students_collection.count_documents({}) == 0:
        sample_students = [
            {"name": "John Smith", "rollNo": "S001", "department": "Computer Science"},
            {"name": "Emma Johnson", "rollNo": "S002", "department": "Electrical Engineering"},
            {"name": "Michael Brown", "rollNo": "S003", "department": "Mechanical Engineering"},
            {"name": "Sophia Williams", "rollNo": "S004", "department": "Civil Engineering"}
        ]
        students_collection.insert_many(sample_students)
        print("Sample student data inserted successfully")
    
    print("MongoDB connection successful")
except Exception as e:
    print(f"MongoDB connection error: {e}")

# Parse MongoDB data to JSON
def parse_json(data):
    return json.loads(json_util.dumps(data))

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
    app.run(debug=True, port=5000)
