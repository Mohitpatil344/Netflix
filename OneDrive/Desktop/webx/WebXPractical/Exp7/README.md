# MongoDB REST API - Experiment 7

This experiment demonstrates CRUD operations in MongoDB using Flask RESTful APIs.

## Prerequisites

1. Python 3.6 or higher
2. MongoDB installed and running on localhost:27017
3. Python packages: Flask, PyMongo

## Installation

1. Install required packages:
```
pip install flask pymongo
```

2. Make sure MongoDB is running on your system:
   - Windows: Start MongoDB service
   - Linux/Mac: `sudo systemctl start mongod` or `brew services start mongodb-community`

## API Descriptions

This experiment includes four separate Flask applications:

### 1. Students API (students.py)
- Endpoint: GET `/students`
- Function: Fetches all documents from the students collection in MongoDB
- Run with: `python students.py`
- Access at: http://localhost:5000/students

### 2. Employees API (employees.py)
- Endpoint: GET `/employees`
- Function: Fetches all documents from the employees collection in MongoDB
- Run with: `python employees.py`
- Access at: http://localhost:5001/employees

### 3. Staff API (staff-route.py)
- Endpoint: GET `/staff`
- Function: Fetches all documents from the staff collection in MongoDB
- Run with: `python staff-route.py`
- Access at: http://localhost:5002/staff

### 4. Add Student API (add-student.py)
- Endpoint: POST `/add-student`
- Function: Adds a new student document to the students collection in MongoDB
- Run with: `python add-student.py`
- Access at: http://localhost:5003/add-student
- Also includes a GET `/students` endpoint for testing

## Testing the APIs

### GET APIs
Simply access the endpoints in your browser or use tools like Postman.

### POST API
Use Postman or curl to send POST requests to the add-student endpoint:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"Jane Doe","rollNo":"S005","department":"Physics"}' http://localhost:5003/add-student
```

Example JSON payload:
```json
{
  "name": "Jane Doe",
  "rollNo": "S005",
  "department": "Physics"
}
```

## Sample Data

Each API will automatically seed its collection with sample data if the collection is empty.

## Note

These are separate applications. You'll need to run each one separately if you want to test all endpoints. 