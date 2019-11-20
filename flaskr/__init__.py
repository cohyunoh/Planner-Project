"""
    This is the init script for flaskr.
"""
from os import urandom
from flask import Flask

APP = Flask(__name__)

APP.secret_key = urandom(32)
