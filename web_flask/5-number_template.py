#!/usr/bin/python3
"""
    flask app
"""

from flask import Flask, escape, render_template
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
def c_route(text):
    """
        display text
    """
    text = escape(text.replace('_', ' '))
    return f"C {text}"

@app.route('/python/<text>', strict_slashes=False)
def py_route(text):
    text = escape(text.replace('_', ' '))
    return f"python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
    """
        n must be ab integer number
    """
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template_route(n):
    """
        display HTML page only if n is an integer
    """
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
