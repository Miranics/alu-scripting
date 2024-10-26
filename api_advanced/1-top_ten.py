#!/usr/bin/python3
"""A module to query the Reddit API for hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if res.status_code != 200:
        print(None)
    else:
        json_response = res.json()
        posts = json_response.get("data").get("children")
        for post in posts:
            print(post.get("data").get("title"))
        print("OK")  # This is where we print the two-character "OK"
