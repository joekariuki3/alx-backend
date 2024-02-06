#!/usr/bin/env python3
"""basic flask app that supports different languages"""

from flask import Flask, render_template, request
from flask_babel import Babel
from datetime import datetime, timezone

app = Flask(__name__)


class Config:
    """Config class containing configurations of our application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# babel = Babel(app, locale_selector=get_locale)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """get the prefered language from the client
    when we recieve a request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """returns the home default page"""
    return render_template('3-index.html')


if __name__ == '__main__':
    """execute only when app.py is run as main"""
    app.run()
