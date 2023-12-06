# app.py
from flask import Flask, render_template

# Create a Flask web application instance
app = Flask(__name__)

# Sample data - a list of dictionaries representing users
users = [
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 30},
    {'name': 'Bob', 'age': 22}
]

# Define a route for the root URL '/'
@app.route('/')
def index():
    # Render the 'index.html' template and pass the 'users' data to it
    return render_template('index.html', users=users)

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
