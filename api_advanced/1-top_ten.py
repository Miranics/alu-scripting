#!/usr/bin/python3
"""Doc"""
import requests


def top_ten(subreddit):
    """Doc"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if res.status_code == 200:
        json_response = res.json()
        posts = json_response.get("data").get("children")
        [print(post.get("data").get("title")) for post in posts]
        print("OK")
    else:
        print("OK")
