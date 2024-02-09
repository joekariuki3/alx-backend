#!/usr/bin/env python3
"""basic flask app that supports different languages"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from datetime import datetime, timezone
from typing import Union

app = Flask(__name__)


users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }


class Config:
    """Config class containing configurations of our application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """get the prefered language from the client
    when we recieve a request"""
    language = request.args.get('locale')
    if language and language in app.config['LANGUAGES']:
        return language
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# babel = Babel(app, locale_selector=get_locale)


def get_user() -> Union[dict, None]:
    """returns a user of id passed as login_as"""
    user_id = request.args.get("login_as")

    if not user_id or not user_id.isdigit():
        return None
    return users.get(int(user_id), None)


@app.before_request
def before_request() -> None:
    """sets global user before other requests are done"""
    g.user = get_user()


@app.route('/')
def home() -> str:
    """returns the home default page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    """execute only when app.py is run as main"""
    app.run()
