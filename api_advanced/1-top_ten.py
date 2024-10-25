#!/usr/bin/python3
"""Checks if a subreddit is valid and prints 'OK' if valid, otherwise 'None'."""
import requests


def top_ten(subreddit):
    """Prints 'OK' for a valid subreddit, and None for an invalid one."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        print("OK")  # Indicate valid subreddit
    else:
        print(None)  # Indicate invalid subreddit
