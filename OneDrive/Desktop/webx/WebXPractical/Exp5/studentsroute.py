from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template with for loop to display student list
students_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Student List</title>
</head>
<body>
    <h1>Student List</h1>
    <p>Here are our students:</p>
    <ul>
        {% for student in students %}
            <li>{{ student }}</li>
        {% endfor %}
    </ul>
    <p>Total students: {{ students|length }}</p>
</body>
</html>
'''

@app.route('/students')
def student_list():
    # List of student names to pass to the template
    students = [
        "John Smith",
        "Emma Johnson",
        "Michael Brown",
        "Sophia Williams",
        "James Davis"
    ]
    
    return render_template_string(students_template, students=students)

if __name__ == '__main__':
    app.run(debug=True)
