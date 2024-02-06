#!/usr/bin/env python3
"""basic flask app that supports different languages"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """returns the home default page
    on route /"""
    return render_template('index.html')


if __name__ == '__main__':
    """execute only when app.py is run as main"""
    app.run()
