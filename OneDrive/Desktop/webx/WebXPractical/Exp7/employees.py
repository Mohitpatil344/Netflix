from flask import Flask, jsonify
from pymongo import MongoClient
import json
from bson import json_util

app = Flask(__name__)

# Connect to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["company_db"]  # Database name
    employees_collection = db["employees"]  # Collection name
    
    # Insert sample data if collection is empty
    if employees_collection.count_documents({}) == 0:
        sample_employees = [
            {"name": "David Johnson", "employeeId": "E001", "department": "HR", "salary": 50000},
            {"name": "Sarah Miller", "employeeId": "E002", "department": "Finance", "salary": 60000},
            {"name": "Robert Wilson", "employeeId": "E003", "department": "IT", "salary": 70000},
            {"name": "Jennifer Taylor", "employeeId": "E004", "department": "Marketing", "salary": 55000},
            {"name": "Thomas Anderson", "employeeId": "E005", "department": "IT", "salary": 72000}
        ]
        employees_collection.insert_many(sample_employees)
        print("Sample employee data inserted successfully")
    
    print("MongoDB connection successful")
except Exception as e:
    print(f"MongoDB connection error: {e}")

# Parse MongoDB data to JSON
def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.route('/employees', methods=['GET'])
def get_employees():
    try:
        employees = list(employees_collection.find({}))
        return jsonify({
            "success": True,
            "employees": parse_json(employees),
            "count": len(employees)
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
