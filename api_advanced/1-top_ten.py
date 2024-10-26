#!/usr/bin/python3
"""
Reddit Top Ten Posts

Fetches and prints the titles of the first 10 hot posts from a given subreddit.

Example:
    To use this module, import it and call the function:
        >>> from top_ten_module import top_ten
        >>> top_ten('subreddit_name')

    Or run it directly in the command line:
        $ python3 1-top_ten.py <subreddit_name>

Functions:
    top_ten(subreddit): Fetches and prints the titles of the first 10 hot posts
    for a given subreddit. Prints "None" if the subreddit is invalid or there
    is an error.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None. Prints the titles of the posts or "None" if an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    posts = response.json().get("data", {}).get("children", [])
    if not posts:
        print("None")
        return

    for post in posts:
        print(post.get("data", {}).get("title", ""))


# Command-line execution
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please provide a subreddit to search.")
    else:
        top_ten(sys.argv[1])
