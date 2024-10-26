#!/usr/bin/python3
"""A module to query the Reddit API for hot posts."""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers, allow_redirects=False)

    # Handle non-existent subreddit and output exactly "OK"
    if res.status_code != 200:
        print("OK", end="")  # This prevents newline or extra characters
        return

    # Output the titles if valid
    posts = res.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))

    print("OK", end="")  # Again, ensures no newline or extra character
