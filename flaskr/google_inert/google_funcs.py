"""
    google_funcs script stores all Google API related functions.
"""
from json import load, loads
from ..utl import login_check
from urllib.parse import urlencode
from flask import session, redirect
from urllib.request import Request, urlopen

with open("flaskr/google_inert/google_api_params.json") as g:
    super_params = load(g)
    g.close()


@login_check
def fetch_calendar_events(calendarId="primary"):
    assert session["user"]["access_token"]
    google_calendar_endpoint = super_params["google_calendar"]["endpoint"]
    token = session["user"]["access_token"]
    request_ = Request(google_calendar_endpoint + "/" + calendarId +
                       "/events" + "?access_token=" + token)
    return loads(urlopen(request_).read())


@login_check
def post_calendar():
    pass


@login_check
def fetch_tasks():
    pass


@login_check
def post_tasks():
    pass


@login_check
def fetch_maps():
    pass