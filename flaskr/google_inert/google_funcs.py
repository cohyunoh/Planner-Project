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
    google_calendar_url = super_params["google_calendar"]["url"]
    token = session["user"]["access_token"]
    request_ = Request(google_calendar_url + "/" + calendarId + "/events" +
                       "?access_token=" + token)
    return loads(urlopen(request_).read())


@login_check
def post_calendar():
    pass


@login_check
def fetch_tasklists(endpoint="/users/@me/lists"):
    assert session["user"]["access_token"]
    google_tasks_url = super_params["google_tasks"]["url"]
    token = session["user"]["access_token"]
    request_ = Request(google_tasks_url + endpoint + "?access_token=" + token)
    return loads(urlopen(request_).read())


@login_check
def fetch_tasks():
    tasklists = fetch_tasklists()["items"]
    tasklists_ids = [item["id"] for item in tasklists]
    google_tasks_url = super_params["google_tasks"]["url"]
    token = session["user"]["access_token"]
    tasks = []
    for tasklists_id in tasklists_ids:
        request_ = Request(google_tasks_url + "/lists/" + tasklists_id +
                           "/tasks" + "?access_token=" + token)
        tasks.append(loads(urlopen(request_).read()))
    return tasks


@login_check
def post_tasks():
    pass


@login_check
def fetch_maps():
    pass