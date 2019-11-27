"""
    GOogle API blueprint module
"""
from copy import deepcopy
from os import path, environ
from json import load, loads
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Blueprint, session, redirect, current_app
from ..utl import register, google, login_check, check_user, add_user, credentials_check

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
    return redirect("/")
