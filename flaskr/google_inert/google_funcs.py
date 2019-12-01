"""
    google_funcs script stores all Google API related functions.
"""
from ..utl import login_check
from urllib.parse import urlencode
from json import load, loads, dumps
from flask import session, redirect
from urllib.request import Request, urlopen

with open("flaskr/google_inert/parameters/google_api_params.json") as g:
    params = load(g)
    g.close()


@login_check
def fetch_userinfo():
    """
        Fetch user information from Google 
    """
    assert session["user"]["access_token"]
    google_userinfo_endpoint = params["google_userinfo"]["endpoint"]
    token = session["user"]["access_token"]
    request_ = Request(google_userinfo_endpoint + "?access_token=" + token)
    return loads(urlopen(request_).read())


@login_check
def fetch_calendar_events(calendarId="primary"):
    """
        Fetch Google Calendar events from Google
    """
    assert session["user"]["access_token"]
    google_calendar_endpoint = params["google_calendar"]["endpoint"]
    token = session["user"]["access_token"]
    request_ = Request(google_calendar_endpoint + "/" + calendarId +
                       "/events" + "?access_token=" + token)
    return loads(urlopen(request_).read())


@login_check
def delete_calendar(eventId, calendarId="primary"):
    """
        Delete a Google Calendar event
    """
    assert session["user"]["access_token"]
    google_calendar_endpoint = params["google_calendar"]["endpoint"]
    token = session["user"]["access_token"]
    request_ = Request(google_calendar_endpoint + "/" + calendarId +
                       "/events/" + eventId + "?access_token=" + token,
                       method="DELETE")
    urlopen(request_)


@login_check
def add_calendar_event(summary, start, end, calendarId="primary"):
    """
        Add Google Calendar event
    """
    assert session["user"]["access_token"]
    google_calendar_endpoint = params["google_calendar"]["endpoint"]
    token = session["user"]["access_token"]
    data = urlencode({"summary": summary, "start": start, "end": end}).encode()
    urlopen(
        Request(google_calendar_endpoint + "/" + calendarId + "/events" +
                "?access_token=" + token,
                data=data,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + token,
                },
                method="POST"))


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
    return [tasklists_ids, tasks]


@login_check
def delete_tasks(tasklistId, taskId):
    assert session["user"]["access_token"]
    google_tasks_endpoint = params["google_tasks"]["endpoint"]
    token = session["user"]["access_token"]
    request_ = Request(google_tasks_endpoint + "/lists/" + tasklistId +
                       "/tasks/" + taskId + "?access_token=" + token,
                       method="DELETE")
    urlopen(request_)


@login_check
def add_task(tasklistId, title, notes):
    assert session["user"]["access_token"]
    google_tasks_endpoint = params["google_tasks"]["endpoint"]
    token = session["user"]["access_token"]
    data = urlencode({"title": title, "notes": notes}).encode()
    urlopen(
        Request(google_tasks_endpoint + "/lists/" + tasklistId + "/tasks" +
                "?access_token=" + token,
                data=data,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + token,
                },
                method="POST"))
