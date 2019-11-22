"""
    GOogle API blueprint module
"""
from os import path
from copy import deepcopy
from json import load, loads
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Blueprint, session, redirect
from ..utl import register, google, login_check

creds = {}

if path.exists("creds.json"):
    with open("creds.json") as f:
        creds = load(f)
        f.close()

if path.exists("flaskr/google_inert/google_api_params.json"):
    with open("flaskr/google_inert/google_api_params.json") as g:
        super_params = load(g)
        g.close()

GOOGLE = Blueprint("GOOGLE", __name__)

GOOGLE_AUTH = deepcopy(google)

google_auth_request_params = super_params["google_auth_request_params"]
google_auth_request_params[
    "client_id"] = creds["google_client_id"] if creds else ""
GOOGLE_AUTH.populate_request(google_auth_request_params)

google_auth_callback_params = super_params["google_auth_callback_params"]
google_auth_callback_params[
    "client_id"] = creds["google_client_id"] if creds else ""
google_auth_callback_params[
    "client_secret"] = creds["google_client_secret"] if creds else ""
GOOGLE_AUTH.populate_callback(google_auth_callback_params)


@GOOGLE.route("/google/oauth2")
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
    return redirect("/")
