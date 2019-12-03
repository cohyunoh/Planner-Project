"""
    Custom Flask decorators
"""
from time import time
from os import environ
from functools import wraps
from ..db.user import get_from_user
from flask import session, redirect, flash


def login_check(f):
    """
        Enforce login required for Flask routes
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect("/")

        return f(*args, **kwargs)

    return decorated_function


def credentials_check(f):
    """
        Enforce credentials requirement for OAuth2 authentication
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not environ.get("GOOGLE_CLIENT_ID", ""):
            flash("Invalid Credentials: Missing Google OAuth2 Credentials")
            return redirect("/")
        if not environ.get("GOOGLE_CLIENT_SECRET", ""):
            flash("Invalid Credentials: Missing Google OAuth2 Credentials")
            return redirect("/")

        return f(*args, **kwargs)

    return decorated_function
