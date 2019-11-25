"""
    user.py facilitate user operations with SQLite3.
"""
from flask import g
from sqlite3 import DatabaseError


def check_user(email):
    """
        Validates if an user already exists in the database.
    """
    try:
        cur = g.db.cursor()
        cur.execute("SELECT email FROM users WHERE email = '%s'" % email)
        user = cur.fetchall()[0]
        cur.close()
        return not user
    except DatabaseError:
        return False


def add_user(email):
    """
        Adds a user to the database.
    """
    try:
        cur = g.db.cursor()
        cur.execute(
            "INSERT INTO users VALUES(NULL, NULL, %s, NULL, NULL, NULL)" %
            email)
        g.db.commit()
        cur.close()
        return True
    except DatabaseError:
        return False