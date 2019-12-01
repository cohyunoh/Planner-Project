"""
    user.py facilitate user operations with SQLite3.
"""
from flask import g
from sqlite3 import DatabaseError


def get_from_user(email, attribute):
    """
        Get an attribute from a user
    """
    try:
        cur = g.db.cursor()
        cur.execute("SELECT %s FROM users WHERE email = '%s'" %
                    (attribute, email))
        attribute = cur.fetchone()
        cur.close()
        if attribute is None:
            return ""
        return attribute[0]
    except DatabaseError:
        raise DatabaseError


def add_user(name, email):
    """
        Adds a user to the database.
    """
    try:
        if not get_from_user(email, "email"):
            cur = g.db.cursor()
            cur.execute(
                "INSERT INTO users VALUES(NULL, '%s', '%s', NULL, NULL, NULL)"
                % (name, email))
            g.db.commit()
            cur.close()
    except DatabaseError:
        raise DatabaseError


def change_user_settings(email, home_address, work_address, news_preference):
    """
        Change the user settings
    """
    try:
        if get_from_user(email, "email"):
            cur = g.db.cursor()
            cur.execute("""
                    UPDATE users
                    SET homeAddress = '%s', 
                    workAddress = '%s', 
                    newsPreference = '%s' 
                    WHERE email = '%s'
                """ % (home_address, work_address, news_preference, email))
            g.db.commit()
            cur.close()
    except DatabaseError:
        raise DatabaseError
