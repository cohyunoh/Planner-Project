"""
    Reddit News View
"""
from .reddit_funcs import get_posts
from ..utl import login_check, get_from_user
from flask import Blueprint, render_template, session

REDDIT = Blueprint("REDDIT", __name__)


@REDDIT.route("/news")
@login_check
def news():
    news = get_posts(get_from_user(session["user"]["email"], "newsPreference"),
                     "top", 15)
    return render_template("news.html", news=news)