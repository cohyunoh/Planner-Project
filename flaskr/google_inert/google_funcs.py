"""
    google_funcs script stores all Google API related functions.
"""
from urllib.error import URLError
from ..utl import login_check
from urllib.parse import urlencode
from json import load, loads, dumps
from flask import session, redirect, flash
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
    try:
        urlopen(
            Request(google_calendar_endpoint + "/" + calendarId + "/events/" +
                    eventId + "?access_token=" + token,
                    method="DELETE"))
    except URLError as e:
        flash(e.reason)


@login_check
def add_calendar_event(summary, description, start, end, calendarId="primary"):
    """
        Add Google Calendar event
    """
    assert session["user"]["access_token"]
    google_calendar_endpoint = params["google_calendar"]["endpoint"]
    token = session["user"]["access_token"]
    data = {
        'summary': summary,
        'description': description,
        'start': start,
        'end': end
    }
    print(data)
    try:
        urlopen(
            Request(google_calendar_endpoint + "/" + calendarId + "/events" +
                    "?access_token=" + token,
                    headers={'Content-Type': 'application/json'},
                    data=dumps(data).encode(),
                    method="POST"))
    except URLError as e:
        print(e.read())
        flash(e.reason)


@login_check
def fetch_tasklists(endpoint="/users/@me/lists"):
    """
        Fetch all Google Tasks tasklists for the user
    """
    assert session["user"]["access_token"]
    google_tasks_endpoint = params["google_tasks"]["endpoint"]
    token = session["user"]["access_token"]
    request_ = Request(google_tasks_endpoint + endpoint + "?access_token=" +
                       token)
    return loads(urlopen(request_).read())


@login_check
def fetch_tasks():
    """
        Fetch all Google Tasks tasks for each tasklist for the user
    """
    tasklists = fetch_tasklists()["items"]
    tasklists_reduced = [{
        "id": item["id"],
        "title": item["title"]
    } for item in tasklists]
    google_tasks_endpoint = params["google_tasks"]["endpoint"]
    token = session["user"]["access_token"]
    tasks = []
    for tasklist in tasklists_reduced:
        request_ = Request(google_tasks_endpoint + "/lists/" + tasklist["id"] +
                           "/tasks" + "?access_token=" + token)
        tasks.append(loads(urlopen(request_).read()))
    return [tasklists_reduced, tasks]


@login_check
def delete_tasks(tasklistId, taskId):
    """
        Delete a task for the user
    """
    assert session["user"]["access_token"]
    google_tasks_endpoint = params["google_tasks"]["endpoint"]
    token = session["user"]["access_token"]
    try:
        urlopen(
            Request(google_tasks_endpoint + "/lists/" + tasklistId +
                    "/tasks/" + taskId + "?access_token=" + token,
                    method="DELETE"))
    except URLError as e:
        flash(e.reason)


@login_check
def add_task(tasklistId, title, notes):
    """
        Add a task for the user
    """
    assert session["user"]["access_token"]
    google_tasks_endpoint = params["google_tasks"]["endpoint"]
    token = session["user"]["access_token"]
    data = {"title": title, "notes": notes}
    try:
        urlopen(
            Request(google_tasks_endpoint + "/lists/" + tasklistId + "/tasks" +
                    "?access_token=" + token,
                    headers={"Content-Type": "application/json"},
                    data=dumps(data).encode(),
                    method="POST"))
    except URLError as e:
        flash(e.reason)


@login_check
def add_task_list(title):
    """
        Add a task list for the user
    """
    assert session["user"]["access_token"]
    google_tasks_endpoint = params["google_tasks"]["endpoint"]
    token = session["user"]["access_token"]
    data = {"title": title}
    try:
        urlopen(
            Request(google_tasks_endpoint + "/users/@me/lists?access_token=" +
                    token,
                    headers={"Content-Type": "application/json"},
                    data=dumps(data).encode(),
                    method="POST"))
    except URLError as e:
        print(e.read().decode("utf8", 'ignore'))
        flash(e.reason)