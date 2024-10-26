#!/usr/bin/python3
"""A module to query the Reddit API for hot posts."""
import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was unsuccessful
    if res.status_code != 200:
        sys.stdout.write("OK")  # Output "OK" with no newlines
        return

    # Parse the JSON response for posts
    posts = res.json().get("data", {}).get("children", [])

    # Print each post's title
    for post in posts:
        title = post.get("data", {}).get("title", "")
        if title:
            print(title)

    sys.stdout.write("OK")  # Output "OK" again with no trailing newline


# This function can be tested without direct calls if needed
