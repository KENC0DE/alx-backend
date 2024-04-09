#!/usr/bin/env python3
"""
Bable
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """Babel configuration"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


def get_user():
    """
    returns a user dictionary or None
    if the ID cannot be found or if login_as was not passed
    """
    return None


@app.before_request
def before_request() -> None:
    """Executes before request"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """locale getter"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """set lang"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
