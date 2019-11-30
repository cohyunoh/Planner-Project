"""
    google_funcs script stores all Google API related functions.
"""
from json import load, loads
from ..utl import login_check
from urllib.parse import urlencode
from flask import session, redirect
from urllib.request import Request, urlopen

with open("flaskr/google_inert/parameters/google_api_params.json") as g:
    params = load(g)
    g.close()


@login_check
def fetch_userinfo():
    assert session["user"]["access_token"]
    google_userinfo_endpoint = params["google_userinfo"]["endpoint"]
    token = session["user"]["access_token"]
    request_ = Request(google_userinfo_endpoint + "?access_token=" + token)
    return loads(urlopen(request_).read())


@login_check
def fetch_calendar_events(calendarId="primary"):
    assert session["user"]["access_token"]
    google_calendar_endpoint = params["google_calendar"]["endpoint"]
    token = session["user"]["access_token"]
    request_ = Request(google_calendar_endpoint + "/" + calendarId +
                       "/events" + "?access_token=" + token)
    return loads(urlopen(request_).read())


@login_check
def post_calendar():
    pass


@login_check
def fetch_tasklists(endpoint="/users/@me/lists"):
    assert session["user"]["access_token"]
    google_tasks_endpoint = params["google_tasks"]["endpoint"]
    token = session["user"]["access_token"]
    request_ = Request(google_tasks_endpoint + endpoint + "?access_token=" +
                       token)
    return loads(urlopen(request_).read())


@login_check
def fetch_tasks():
    tasklists = fetch_tasklists()["items"]
    tasklists_ids = [item["id"] for item in tasklists]
    google_tasks_endpoint = params["google_tasks"]["endpoint"]
    token = session["user"]["access_token"]
    tasks = []
    for tasklists_id in tasklists_ids:
        request_ = Request(google_tasks_endpoint + "/lists/" + tasklists_id +
                           "/tasks" + "?access_token=" + token)
        tasks.append(loads(urlopen(request_).read()))
    return tasks


@login_check
def post_tasks():
    pass


@login_check
def fetch_maps():
    pass