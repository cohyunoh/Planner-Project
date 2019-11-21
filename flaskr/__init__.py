"""
    This is the init script for flaskr.
"""
from os import urandom
from flask import Flask, render_template, session, redirect, url_for
from .google import GOOGLE
from .utl.pdecorators.flask_decorators import login_check

APP = Flask(__name__)

APP.secret_key = urandom(32)

APP.register_blueprint(GOOGLE)


@APP.route("/")
@login_check
def index():
    return render_template("index.html")


@APP.route("/home")
@login_check
def home():
    return render_template("home.html")