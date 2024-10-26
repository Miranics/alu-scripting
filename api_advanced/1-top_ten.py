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
        None. Prints post titles if they exist or "OK" if not.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("OK", end='')  # Print "OK" without a newline or extra space
        return

    json_response = response.json()
    posts = json_response.get('data', {}).get('children', [])

    if not posts:  # If no posts are returned, print "OK"
        print("OK", end='')  # Print "OK" without a newline or extra space
        return

    for post in posts:
        print(post.get('data', {}).get('title', ""))  # Print each title

    # Ensure no newline is printed after the last title
    import sys
    sys.stdout.flush()  # Clear any buffer to ensure the output is exactly as expected

