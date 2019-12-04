"""
    Reddit News View
"""
from .reddit_funcs import get_posts
from ..utl import login_check, get_from_user
from flask import Blueprint, render_template, session, request

REDDIT = Blueprint("REDDIT", __name__)


@REDDIT.route("/news")
@REDDIT.route("/reddit/sort")
@login_check
def news():
    preference = "top"
    if "sortBy" in request.args:
        preference = request.args["sortBy"].lower()
    news = get_posts(get_from_user(session["user"]["email"], "newsPreference"),
                     preference, 15)
    return render_template("news.html", news=news)