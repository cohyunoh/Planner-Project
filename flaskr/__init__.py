"""
    Initialize a Flask instance
"""
from os import urandom
from time import sleep
from sqlite3 import connect
from .reddit import get_posts
from datetime import date, datetime
from .utl import login_check, conn, close, change_user_settings, get_from_user
from flask import Flask, render_template, session, redirect, url_for, g, request
from .google_inert import (GOOGLE, fetch_calendar_events, fetch_tasks,
                           fetch_userinfo, delete_calendar, delete_tasks,
                           add_calendar_event, add_task)

APP = Flask(__name__)

APP.secret_key = urandom(32)

APP.config.from_mapping(DATABASE="flaskr/database.db")

APP.jinja_env.globals.update(zip=zip)

with open("flaskr/database.db", "w+") as f:
    db = connect(APP.config["DATABASE"])
    with open("flaskr/schema.sql") as g:
        db.executescript(g.read())
        g.close()
        db.close()
    f.close()

APP.register_blueprint(GOOGLE)


@APP.before_request
def database_connection():
    """
        Handle automatic request based database connection
    """
    conn()


@APP.teardown_request
def close_database_connection(Exception):
    """
        Teardown database connection at the end of a request
    """
    close()


@APP.route("/")
def index():
    """
        Index routes the app to public views or protected views
    """
    if "user" in session:
        return redirect(url_for("home"))
    return render_template("index.html")


@APP.route("/registration")
@login_check
def registration():
    """
        Registration view for the Flask app
    """
    return render_template("registration.html")


@APP.route("/home")
@login_check
def home():
    """
        Renders the homepage
    """
    datetime = date.today()
    name = get_from_user(session["user"]["email"], "name")
    calendar_events = fetch_calendar_events()["items"]
    tasklist_ids, tasks = fetch_tasks()
    session["user"]["selected_tasklist_id"] = tasklist_ids[0]
    news = get_posts(get_from_user(session["user"]["email"], "newsPreference"),
                     "top", 5)
    return render_template("home.html",
                           datetime=datetime,
                           name=name,
                           calendar=calendar_events,
                           tasklist_ids=tasklist_ids,
                           tasks=tasks,
                           news=news)


@APP.route("/settings")
@login_check
def settings():
    """
        Render the settings.html template for the Flask app
    """
    home_address = get_from_user(session["user"]["email"],
                                 "homeAddress").split(",")
    work_address = get_from_user(session["user"]["email"],
                                 "workAddress").split(",")
    news_preference = get_from_user(session["user"]["email"], "newsPreference")
    return render_template("settings.html",
                           news_preference=news_preference,
                           home_address=home_address[0],
                           home_address2=home_address[1],
                           home_city=home_address[2],
                           home_state=home_address[3],
                           home_zip=home_address[4],
                           work_address=work_address[0],
                           work_address2=work_address[1],
                           work_city=work_address[2],
                           work_state=work_address[3],
                           work_zip=work_address[4])


@APP.route("/register")
@APP.route("/changesettings")
def change_settings():
    """
        Handle the registration/change settings functionality of the app
    """
    home_address = [
        request.args["homeAddress"], request.args["homeAddress2"],
        request.args["homeCity"], request.args["homeState"],
        request.args["homeZip"]
    ]
    work_address = [
        request.args["workAddress"], request.args["workAddress2"],
        request.args["workCity"], request.args["workState"],
        request.args["workZip"]
    ]
    change_user_settings(session["user"]["email"], ",".join(home_address),
                         ",".join(work_address), request.args["inputNews"])
    if "settings" in request.args:
        return redirect(url_for("settings"))
    return redirect(url_for("index"))


@APP.route("/news")
@login_check
def news():
    news = get_posts(get_from_user(session["user"]["email"], "newsPreference"),
                     "top", 15)
    return render_template("news.html", news=news)


@APP.route("/remove")
@login_check
def remove():
    if "google_calendar" in request.args:
        delete_calendar(request.args["event_id"])
    if "google_tasks" in request.args:
        delete_tasks(request.args["task_list_id"], request.args["task_id"])
    return redirect(url_for("index"))


@APP.route("/add/calendar")
@APP.route("/add/tasks")
@login_check
def add():
    if "google_calendar" in request.args:
        start = {
            "dateTime": request.args["eventStart"],
            "timeZone": "America/New_York"
        }
        end = {
            "dateTime": request.args["eventEnd"],
            "timeZone": "America/New_York"
        }
        add_calendar_event(request.args["eventSummary"], start, end)
    if "google_tasks" in request.args:
        task_list_id = session["user"]["selected_tasklist_id"]
        add_task(task_list_id, request.args["taskTitle"],
                 request.args["taskNotes"])
    return redirect(url_for("index"))


@APP.route("/logout")
@login_check
def logout():
    """
        Handle the logout operation for the Flask app
    """
    session.pop("user", None)
    return redirect(url_for("index"))
