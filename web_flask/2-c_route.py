#!/usr/bin/python3
"""
    flask app
"""

from flask import Flask, escape
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        for the /hbnb route
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
        display text
    """
    text = escape(text.replace('_', ' '))
    return f"C {text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)