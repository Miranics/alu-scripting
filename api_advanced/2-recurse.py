#!/usr/bin/python3
""""Doc"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Retrieve hot posts from a subreddit recursively.
    Reddit sends an 'after' property in the response, and
    the function will keep retrieving posts until 'after' is null.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}
    param = {"after": after}
    res = requests.get(url, headers=header, params=param)

    if res.status_code != 200:
        return None

    json_res = res.json()
    after = json_res.get("data").get("after")
    has_next = after is not None
    hot_articles = json_res.get("data").get("children")

    # Collect the titles of the hot posts
    for article in hot_articles:
        hot_list.append(article.get("data").get("title"))

    # Recurse if there are more posts to retrieve
    return recurse(subreddit, hot_list, after=after) if has_next else hot_list
