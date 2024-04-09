#!/usr/bin/env python3
"""
Simple flask application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welCome() -> str:
    """Welcome Route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
