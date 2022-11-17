"""A basic Flask application to show the general framework."""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Define main route into the website."""
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
