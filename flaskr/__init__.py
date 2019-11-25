"""
    Initialize a Flask instance
"""
from os import urandom, path
from .utl import login_check, conn, close
from .google_inert import GOOGLE, fetch_calendar_events, fetch_tasks
from flask import Flask, render_template, session, redirect, url_for, g

APP = Flask(__name__)

APP.secret_key = urandom(32)

if not path.exists("flaskr/data/database.db"):
    with open("flaskr/data/database.db", "w+") as f:
        f.close()

APP.config.from_mapping(DATABASE="flaskr/data/database.db")

APP.register_blueprint(GOOGLE)

with APP.app_context():
    conn()
    with APP.open_resource("flaskr/schema.sql") as f:
        g.db.executescript(f.read().decode("utf8"))
    close()


@APP.before_request
def database_connection():
    conn()


@APP.teardown_request
def close_database_connection(Exception):
    close()


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
    return render_template("index.html", is_logged_in=False)


@APP.route("/home")
@login_check
def home():
    """
        Renders the homepage
    """
    calendar_events = fetch_calendar_events()["items"]
    tasks = fetch_tasks()
    return render_template("home.html", calendar=calendar_events, tasks=tasks)


@APP.route("/logout")
@login_check
def logout():
    session.pop("user", None)
    return redirect("/")