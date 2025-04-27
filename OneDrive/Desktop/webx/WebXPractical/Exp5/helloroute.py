from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template for greeting users
hello_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Hello {{ name }}</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
    <p>Welcome to our Flask application.</p>
    <p>The current URL path is: /hello/{{ name }}</p>
</body>
</html>
'''

@app.route('/hello/<string:name>')
def hello(name):
    return render_template_string(hello_template, name=name)

if __name__ == '__main__':
    app.run(debug=True) 