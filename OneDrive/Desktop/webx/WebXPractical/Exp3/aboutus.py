from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to our Flask Website!</h1>'

@app.route('/about')
def about():
    return '<h2>About Us</h2><p>We are a company specializing in web development using Flask framework.</p>'

if __name__ == '__main__':
    app.run(debug=True)
