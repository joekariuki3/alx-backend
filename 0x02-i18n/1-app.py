#!/usr/bin/env python3
"""basic flask app that supports different languages"""

from flask import Flask, render_template, request
from flask_babel import Babel
from datetime import datetime, timezone

app = Flask(__name__)


class Config:
    """Config class containing configurations of our application"""
    LANGUAGES = ["en", "fr"]

    def get_locale(self):
        """set the default language to english en"""
        return self.LANGUAGES[0]

    def get_timezone(self):
        """set the default timezone to utc"""
        return timezone.utc


babel = Babel(app,
              locale_selector=Config.get_locale,
              timezone_selector=Config.get_timezone)


@app.route('/')
def home():
    """returns the home default page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    """execute only when app.py is run as main"""
    app.run()
