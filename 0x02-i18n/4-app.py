#!/usr/bin/env python3
"""
Bable
"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """locale getter"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """set lang"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
