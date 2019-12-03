"""
    Google API blueprint module
"""
from copy import deepcopy
from os import path, environ
from json import load, loads
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Blueprint, session, redirect, current_app, url_for, request
from .google_funcs import fetch_userinfo, add_calendar_event, add_task, add_task_list
from ..utl import register, google, login_check, add_user, credentials_check, get_from_user

with open("flaskr/google_inert/parameters/google_api_params.json") as g:
    params = load(g)
    g.close()

GOOGLE = Blueprint("GOOGLE", __name__)

GOOGLE_AUTH = deepcopy(google)

requests_ = params["google_auth_request_params"]
requests_["client_id"] = environ.get("GOOGLE_CLIENT_ID", "")
GOOGLE_AUTH.populate_request(requests_)

callbacks_ = params["google_auth_callback_params"]
callbacks_["client_id"] = requests_["client_id"]
callbacks_["client_secret"] = environ.get("GOOGLE_CLIENT_SECRET", "")
GOOGLE_AUTH.populate_callback(callbacks_)


@GOOGLE.route("/google/oauth2")
@credentials_check
@register(GOOGLE_AUTH, "/google/oauth2")
def auth():
    """
        Authentication Flask route that use a flask_oauth2
        wrapper to register the OAuth connection object for
        authentication.
    """
    if "access_token" in session:
        session["user"] = {
            "access_token": session["access_token"],
            "logged_in": True
        }
        session.pop("access_token", None)
        userinfo = fetch_userinfo()
        session["user"]["email"] = userinfo["email"]
        if not get_from_user(userinfo["email"], "email"):
            add_user(userinfo["name"], userinfo["email"])
            return redirect(url_for("registration"))
    return redirect(url_for("index"))


@GOOGLE.route("/add/calendar")
@GOOGLE.route("/add/tasks")
@login_check
def add():
    if "google_calendar" in request.args:
        start = {
            'dateTime':
            request.args['eventStart'] + request.args['timeZoneOffset'],
            'timeZone': request.args['timeZone']
        }
        end = {
            'dateTime':
            request.args['eventEnd'] + request.args['timeZoneOffset'],
            'timeZone': request.args['timeZone']
        }
        add_calendar_event(request.args["eventSummary"],
                           request.args["eventDescription"], start, end)
    if "google_tasks" in request.args:
        task_list_id = request.args["task_list_id"]
        add_task(task_list_id, request.args["task_title"],
                 request.args["task_notes"])
    if "google_task_list" in request.args:
        add_task_list(request.args["task_list_title"])
    return redirect(url_for("index"))