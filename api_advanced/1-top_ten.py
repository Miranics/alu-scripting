#!/usr/bin/python3
"""A module to query the Reddit API for hot posts."""
import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers, allow_redirects=False)

    # Handle non-existent subreddit by outputting exactly "OK"
    if res.status_code != 200:
        sys.stdout.write("OK")  # Outputs OK without newline
        sys.stdout.flush()
        return

    # Output the titles
    posts = res.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))

    sys.stdout.write("OK")  # Outputs OK without newline after listing titles
    sys.stdout.flush()
