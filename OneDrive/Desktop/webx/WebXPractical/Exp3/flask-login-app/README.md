# Flask Login App

This is a simple Flask application that provides a login form. Users can enter their username and password, and upon submission, the application checks for the credentials.

## Features

- Login form with username and password fields
- Validates credentials (username: admin, password: 1234)
- Displays a success message upon successful login

## Project Structure

```
flask-login-app
├── src
│   ├── app.py          # Main entry point of the Flask application
│   ├── templates       # Contains HTML templates
│   │   ├── login.html  # Login form
│   │   └── success.html # Success message
│   └── static          # Contains static files
│       └── styles.css  # CSS styles for the application
├── requirements.txt    # Lists project dependencies
└── README.md           # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-login-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000/login` to access the login form.

## License

This project is licensed under the MIT License.