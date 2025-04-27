from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with form and feedback display
feedback_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Feedback Form</title>
</head>
<body>
    <h1>Feedback Form</h1>
    
    <form action="/feedback" method="POST">
        <div>
            <label for="name">Your Name:</label><br>
            <input type="text" id="name" name="name" required>
        </div>
        <br>
        <div>
            <label for="feedback">Your Feedback:</label><br>
            <textarea id="feedback" name="feedback" rows="5" cols="40" required></textarea>
        </div>
        <br>
        <button type="submit">Submit Feedback</button>
    </form>
    
    {% if submitted %}
    <hr>
    <h2>Submitted Feedback:</h2>
    <p><strong>Name:</strong> {{ name }}</p>
    <p><strong>Feedback:</strong> {{ feedback }}</p>
    <p><strong>Submitted at:</strong> {{ time }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name', '')
        feedback_text = request.form.get('feedback', '')
        
        from datetime import datetime
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        return render_template_string(
            feedback_template, 
            submitted=True, 
            name=name, 
            feedback=feedback_text,
            time=time
        )
    
    return render_template_string(feedback_template, submitted=False)

if __name__ == '__main__':
    app.run(debug=True)
