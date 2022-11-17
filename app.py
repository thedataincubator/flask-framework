"""A Flask application to display stock ticker information."""
from flask import Flask, render_template, request

import requests

app = Flask(__name__)

@app.route('/')
def index():
    """Define main route into the website."""
    return render_template('index.html')

@app.route('/plot')
def plot():
    """Display ticker data based on user-supplied input."""
    #  This is where you need to define what the 'plot' method will do.
    return render_template('plot.html')

if __name__ == '__main__':
    app.run()
