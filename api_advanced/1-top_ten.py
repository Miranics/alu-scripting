#!/usr/bin/python3
"""
Reddit Top Ten Module

This module defines a function that fetches and prints the titles of the first
10 hot posts listed for a given subreddit using the Reddit API.

Example:
    To use this module, import it and call the function:
        >>> from my_module import top_ten
        >>> top_ten('subreddit_name')

    Or run it directly in the command line:
        $ python3 your_script_name.py <subreddit_name>

Functions:
    top_ten(subreddit): Fetches and prints the titles of the first 10 hot posts
    for a given subreddit. If the subreddit does not exist or an error occurs,
    "OK" is printed.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None. Prints the titles of the posts or "OK" if an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if res.status_code == 200:
        json_response = res.json()
        posts = json_response.get("data", {}).get("children", [])
        [print(post.get("data", {}).get("title", "")) for post in posts]
        print("OK")
    else:
        print("OK")
