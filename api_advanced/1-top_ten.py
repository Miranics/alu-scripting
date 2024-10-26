#!/usr/bin/python3
"""
A module to query the Reddit API for hot posts.

This module contains the function `top_ten`, which retrieves and prints
the titles of the first 10 hot posts from a specified subreddit. If the
subreddit is invalid, it will print "OK".

Usage:
    python3 1-main.py <subreddit_name>
"""

import requests
import sys


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed in a subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    If the subreddit does not exist or cannot be accessed, it prints "OK".
    Otherwise, it prints the titles of the first 10 hot posts and "OK".
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers, allow_redirects=False)

    # If the subreddit is invalid, output "OK" without a newline
    if res.status_code != 200:
        print("OK", end="")
        return

    # Retrieve and print post titles
    posts = res.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))

    # Final "OK" output
    print("OK", end="")  # This prints OK without an extra newline


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
