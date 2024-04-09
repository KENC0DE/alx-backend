#!/usr/bin/env python3

"""A simple flask app"""

from typing import Optional, Dict, Any
from flask import Flask, render_template, request, g
from flask_babel import Babel

class Config(object):
    """Babel configuration"""
    LANGUAGES: list[str] = ['en', 'fr']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'

# configure the flask app
app: Flask = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel: Babel = Babel(app)

users: Dict[int, Dict[str, Optional[str]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Optional[Dict[str, Any]]:
    """returns a user dictionary or None if the ID cannot be found"""
    login_id: Optional[str] = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None

@app.before_request
def before_request() -> None:
    """Set the user in the request context"""
    user: Optional[Dict[str, Any]] = get_user()
    g.user = user

@babel.localeselector
def get_locale() -> str:
    """Determine the best match for the supported languages"""
    locale: Optional[str] = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """Render the index template"""
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
