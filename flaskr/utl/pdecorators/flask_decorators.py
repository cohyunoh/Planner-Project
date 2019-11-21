"""
    Custom Flask decorators
"""
from functools import wraps
from flask import session, redirect


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
