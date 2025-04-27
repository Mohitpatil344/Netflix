# AJAX Applications - Experiment 9

This experiment demonstrates the development of Rich Internet Applications using AJAX (Asynchronous JavaScript and XML).

## Description

AJAX allows web pages to be updated asynchronously by exchanging data with a web server behind the scenes. This means that it's possible to update parts of a web page without reloading the whole page.

## Examples Included

### 1. Button with AJAX Request (button.html)
- A simple HTML page with a button
- When the button is clicked, AJAX is used to fetch user data from a remote server
- The received data is displayed on the page without refreshing

### 2. Form with AJAX Submission (form.html)
- A simple form with two fields: Name and Email
- When the form is submitted, AJAX is used to send the data to a server
- The server response is displayed without page reload

### 3. JSON Data Request (json.html)
- A webpage with a button to request JSON data
- When clicked, AJAX is used to fetch a post from a server
- A second button appears to load comments related to the post

## How to Run

These examples can be run in several ways:

### Method 1: Open Directly in Browser
Simply double-click on any HTML file to open it in your browser. However, some AJAX requests might be blocked due to CORS (Cross-Origin Resource Sharing) policies when run this way.

### Method 2: Use a Local Server (Recommended)
For the best experience, use a simple HTTP server:

1. **Using Python:**
   ```
   # For Python 3.x
   python -m http.server
   
   # For Python 2.x
   python -m SimpleHTTPServer
   ```

2. **Using Node.js:**
   ```
   # Install http-server globally
   npm install -g http-server
   
   # Run the server
   http-server
   ```

3. Open your browser and navigate to `http://localhost:8000` (or the port shown in your terminal)

## AJAX Concepts Demonstrated

1. **Creating and Sending Requests**
   - Creating XMLHttpRequest objects
   - Configuring request methods (GET, POST)
   - Setting request headers
   - Sending requests with and without data

2. **Handling Responses**
   - Processing successful responses
   - Error handling
   - Parsing JSON data
   - Updating the DOM with received data

3. **Event Handling**
   - Load events
   - Error events
   - User interaction

## APIs Used

All examples use [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - a free online REST API for testing and prototyping.

## Notes

- These examples use vanilla JavaScript without any libraries or frameworks
- The code uses modern JavaScript features but should work in most modern browsers
- Minimal CSS is used to focus on AJAX functionality
- The examples demonstrate both requesting data and submitting data 