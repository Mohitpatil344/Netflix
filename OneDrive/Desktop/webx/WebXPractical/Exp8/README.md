# AngularJS Experiment - Exp8

This experiment demonstrates AngularJS concepts such as directives, controllers, filters, and data binding.

## Prerequisites

- A web browser
- Internet connection (to load AngularJS from CDN)

## Running the Examples

Each example is a standalone HTML file that can be run directly in your browser. The examples use AngularJS loaded from Google's CDN.

### Method 1: Directly open HTML files
Simply double-click on any HTML file to open it in your default browser.

### Method 2: Using a local server
For the best experience, especially for AJAX requests, use a simple HTTP server:

1. **Using Python:**
   ```
   # For Python 3.x
   python -m http.server
   
   # For Python 2.x
   python -m SimpleHTTPServer
   ```

2. **Using Node.js:**
   ```
   # Install http-server globally (if you haven't already)
   npm install -g http-server
   
   # Run the server
   http-server
   ```

3. Open your browser and navigate to `http://localhost:8000` (or the port shown in your terminal)

## Examples Included

### Example 1: Main Controller (mainController.html and mainController.js)
- Demonstrates creating a controller in AngularJS
- Features: Data binding, ng-repeat directive, and expressions
- Run: Open `mainController.html` in your browser

### Example 2: String Uppercase (stringUppercase.html and stringUppercase.js)
- Takes a string input and displays it in uppercase using filters
- Features: Filters, two-way data binding, ng-model directive
- Run: Open `stringUppercase.html` in your browser

### Example 3: User Name (userName.html and userName.js)
- Takes the user's name as input using input boxes
- Features: Forms, ng-model directive, ng-show directive
- Run: Open `userName.html` in your browser

### Example 4: User Age (userAge.html and userAge.js)
- Takes the user's age as input and provides feedback
- Features: Forms, controllers, functions, conditional logic
- Run: Open `userAge.html` in your browser

## AngularJS Concepts Demonstrated

1. **Directives**
   - ng-app: Initializes an AngularJS application
   - ng-controller: Attaches a controller to the view
   - ng-model: Binds an input to a variable
   - ng-repeat: Iterates over a collection
   - ng-show/ng-hide: Shows or hides elements based on expressions

2. **Controllers**
   - Define application behavior
   - Manage the application's data
   - Provide functions for user interaction

3. **Filters**
   - uppercase: Converts text to uppercase
   - currency: Formats numbers as currency

4. **Data Binding**
   - One-way binding: Display data from the scope
   - Two-way binding: Synchronize data between the model and view

## Notes

- These examples use AngularJS 1.8.2 (not to be confused with the newer Angular 2+)
- The examples are designed to be simple and focused on specific concepts
- No build tools or complex setup required 