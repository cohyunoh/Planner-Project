"""
    GOogle API blueprint module
"""
from copy import deepcopy
from json import load
from flask import Blueprint, session
from .utl.flask_oauth2.flask_oauth2.model import register, google

with open("creds.json") as f:
    creds = load(f)

GOOGLE = Blueprint("GOOGLE", __name__)

GOOGLE_AUTH = deepcopy(google)

GOOGLE_AUTH.populate_request({
    "client_id": creds["google_client_id"],
    "response_type": "code",
    "scope": "openid",
    "redirect_uri": "http://localhost:5000/google/oauth2",
    "nonce": True
})
GOOGLE_AUTH.populate_callback({
    "client_id": creds["google_client_id"],
    "client_secret": creds["google_client_secret"],
    "redirect_uri": "http://localhost:5000/google/oauth2",
    "grant_type": "authorization_code"
})


@GOOGLE.route("/google/oauth2")
@register(GOOGLE_AUTH)
def auth():
    if "access_token" in session:
        session["is_logged_in"] = True
    pass
