from flask import Flask, request, render_template_string

app = Flask(__name__)


form_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>User Information Form</title>
</head>
<body>
    <h2>User Information</h2>
    <form action="/form" method="POST">
        <div>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
        </div>
        <br>
        <div>
            <label for="age">Age:</label>
            <input type="number" id="age" name="age" required>
        </div>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
'''

thank_you_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Thank You</title>
</head>
<body>
    <h2>Thank You!</h2>
    <p>Your information has been submitted successfully.</p>
    <p>Name: {{ name }}</p>
    <p>Age: {{ age }}</p>
    <p><a href="/form">Back to Form</a></p>
</body>
</html>
'''

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name', '')
        age = request.form.get('age', '')
        return render_template_string(thank_you_template, name=name, age=age)
    return render_template_string(form_template)

if __name__ == '__main__':
    app.run(debug=True)
