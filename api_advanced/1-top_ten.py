#!/usr/bin/python3
"""
Reddit Top Ten Posts Module

This module queries the Reddit API to fetch and print the titles of the first
10 hot posts listed for a given subreddit.

Usage:
    Call the `top_ten(subreddit)` function with the name of a subreddit to
    retrieve the top 10 hot posts.

Functions:
    top_ten(subreddit): Prints the titles of the first 10 hot posts from the 
                        specified subreddit. If the subreddit is invalid or 
                        has no posts, it prints "OK".
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve posts from.

    Returns:
        None. Prints post titles if they exist or "OK" if not.
    """


#!/usr/bin/python3
""""Doc"""
import requests


def top_ten(subreddit):
    """ "Doc"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if res.status_code != 200:
        print('OK', end='')
    else:
        json_response = res.json()
        posts = json_response.get("data").get("children")
        [print(post.get("data").get("title")) for post in posts]

    # This ensures that there's no trailing newline
    import sys

    sys.stdout.write("")  # This will not add any new lines
