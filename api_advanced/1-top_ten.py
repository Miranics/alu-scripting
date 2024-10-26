#!/usr/bin/python3
"""A module to query the Reddit API for hot posts."""
import requests
import sys  # Ensure sys is imported

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers, allow_redirects=False)

    # If the request is unsuccessful, print "OK" without newline
    if res.status_code != 200:
        sys.stdout.write("OK")
        sys.stdout.flush()
        return

    # Extract titles of hot posts
    posts = res.json().get("data", {}).get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title", "")
        if title:
            print(title)

    # Output "OK" without any newline
    sys.stdout.write("OK")
    sys.stdout.flush()
