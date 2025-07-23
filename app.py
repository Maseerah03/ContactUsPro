from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

# ?? Route 1: Serve the HTML Form Page
@app.route('/')
def index():
    return render_template('index.html')  # Make sure your index.html is inside a folder named 'templates'

# ?? Route 2: Handle Form Submission
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Grab form values
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Save to CSV (simulated database)
        with open('submissions.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, message])

        return "<h2>Thank you for your submission, " + name + "!</h2><a href='/'>Back to form</a>"

# ?? Run the app
if __name__ == '__main__':
    app.run(debug=True)
