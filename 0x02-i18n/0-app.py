#!/usr/bin/env python3
"""
Simple flask application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welCome() -> str:
    """Welcome Route"""
    data = {
        'ttl': 'Welcom to Holberton',
        'msg': 'Hello world'
    }
    return render_template('0-index.html', data=data)


if __name__ == '__main__':
    app.run()
