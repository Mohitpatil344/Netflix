from flask import Flask, request, render_template_string

app = Flask(__name__)

login_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Login Successful</title>
</head>
<body>
    <h2>Login Successful</h2>
    <p>Welcome, {{ username }}!</p>
    <a href="/login">Logout</a>
</body>
</html>
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == '1234':
            return render_template_string(login_template, username=username)
        else:
            error = 'Invalid credentials. Please try again.'
    
    return render_template_string(login_template, error=error)

if __name__ == '__main__':
    app.run(debug=True)
