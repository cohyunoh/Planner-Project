"""
    reddit_funcs script stores all Reddit API related functions.
"""
from json import load, loads
from ..utl import login_check
from urllib.parse import urlencode
from flask import session, redirect
from urllib.request import Request, urlopen

REDDIT_SUBREDDIT = "https://www.reddit.com/r/"


@login_check
def get_posts(subreddit, status, limit=5):
    """
        Fetch posts from a subreddit
    """
    assert session["user"]["access_token"]
    request_ = Request(REDDIT_SUBREDDIT + subreddit + "/" + status +
                       ".json?limit=" + str(limit))
    return loads(urlopen(request_).read())