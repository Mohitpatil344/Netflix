from flask import Flask, jsonify
from pymongo import MongoClient
import json
from bson import json_util

app = Flask(__name__)

# Connect to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["university_db"]  # Database name
    staff_collection = db["staff"]  # Collection name
    
    # Insert sample data if collection is empty
    if staff_collection.count_documents({}) == 0:
        sample_staff = [
            {"name": "Dr. James Wilson", "staffId": "ST001", "position": "Professor", "department": "Physics", "yearsOfService": 15},
            {"name": "Dr. Emily Clark", "staffId": "ST002", "position": "Associate Professor", "department": "Chemistry", "yearsOfService": 8},
            {"name": "Dr. Richard Brown", "staffId": "ST003", "position": "Assistant Professor", "department": "Mathematics", "yearsOfService": 5},
            {"name": "Dr. Linda Martinez", "staffId": "ST004", "position": "Professor", "department": "Computer Science", "yearsOfService": 12},
            {"name": "Mr. Steve Adams", "staffId": "ST005", "position": "Lab Technician", "department": "Biology", "yearsOfService": 7}
        ]
        staff_collection.insert_many(sample_staff)
        print("Sample staff data inserted successfully")
    
    print("MongoDB connection successful")
except Exception as e:
    print(f"MongoDB connection error: {e}")

# Parse MongoDB data to JSON
def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.route('/staff', methods=['GET'])
def get_staff():
    try:
        staff = list(staff_collection.find({}))
        return jsonify({
            "success": True,
            "staff": parse_json(staff),
            "count": len(staff)
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5002)
