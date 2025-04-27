from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template for the home page
home_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
</head>
<body>
    <h1>Welcome to the Home Page</h1>
    <p>This is a static HTML page rendered using render_template_string().</p>
    <p>Flask is a lightweight web framework for Python.</p>
    <ul>
        <li>Easy to use</li>
        <li>Flexible</li>
        <li>Built-in development server</li>
        <li>Supports template rendering</li>
    </ul>
</body>
</html>
'''

@app.route('/home')
def home():
    return render_template_string(home_template)

if __name__ == '__main__':
    app.run(debug=True)
