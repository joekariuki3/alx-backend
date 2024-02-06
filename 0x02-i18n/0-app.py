#!/usr/bin/env python3
"""basic flask app that supports different languages"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """home page"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
