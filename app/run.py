"""
Flask application entry point.

This module acts as the entry point for the Flask application.

Usage:
    The Flask application is initialized here.
    The prediction blueprint ('api.prediction.bp') is registered
    with the application
"""
from api.prediction import bp
from flask import Flask

app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)  # noqa: S201
