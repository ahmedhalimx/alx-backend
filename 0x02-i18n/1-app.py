#!/usr/bin/env python3
"""
Flask application
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Configuration Class Definition
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a html template
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
