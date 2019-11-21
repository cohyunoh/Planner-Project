"""
    Custom Flask decorators
"""
from functools import wraps
from flask import session, redirect


def login_check(f):
    """Enforce login required for Flask routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "is_logged_in" in session:
            if session["is_logged_in"]:
                return redirect("/")
        return f(*args, **kwargs)

    return decorated_function
