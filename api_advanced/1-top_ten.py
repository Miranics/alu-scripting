#!/usr/bin/python3
"""
Reddit Top Ten Posts

This module queries the Reddit API and prints the titles of the first 10
hot posts for a specified subreddit.

Usage:
    Call the `top_ten(subreddit)` function with the name of a subreddit.

Functions:
    - top_ten(subreddit): Prints the titles of the top 10 hot posts of the subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve posts from.

    Returns:
        None. Prints post titles or "None" if an error occurs.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    json_response = response.json()
    posts = json_response.get('data', {}).get('children', [])
    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get('data', {}).get('title', ""))
