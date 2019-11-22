"""
    Initialize a Flask instance
"""
from os import urandom, path
from .utl import login_check
from .google_inert import GOOGLE, fetch_calendar
from flask import Flask, render_template, session, redirect, url_for

APP = Flask(__name__)

APP.secret_key = urandom(32)

if not path.exists("flaskr/data/database.db"):
    with open("flaskr/data/database.db", "w+") as f:
        f.close()

APP.config.from_mapping(DATABASE="data/database.db")

APP.register_blueprint(GOOGLE)


@APP.route("/")
def index():
    """
        Index routes the app to public views or protected
        views.
    """
    if not path.exists("creds.json"):
        return "No credentials found for this Flask app. Check out the readme for instructions."
    if "user" in session:
        return redirect(url_for("home"))
    return render_template("index.html")


@APP.route("/home")
@login_check
def home():
    """
        Renders the homepage
    """
    calendar_ = fetch_calendar()
    return render_template("home.html", calendar=calendar_)
