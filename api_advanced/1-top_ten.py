#!/usr/bin/python3
"""
Reddit Top Ten Posts Module

This script fetches and prints the titles of the first 10 hot posts listed
for a specified subreddit using the Reddit API.

Example:
    To use this script, run the following command:
        $ python3 1-top_ten.py <subreddit_name>

Functions:
    top_ten(subreddit): Queries the Reddit API and prints the titles of the first
    10 hot posts for a given subreddit. Prints "None" if the subreddit is invalid.
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

    # Check if the subreddit is invalid or there's an error in the response
    if response.status_code != 200:
        print("None")
        return

    try:
        # Extracting the top 10 posts' titles
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print("None")
            return
        
        for post in posts[:10]:
            print(post.get("data", {}).get("title", ""))
    except (ValueError, KeyError, TypeError):
        # Handle any unexpected JSON or structure issues gracefully
        print("None")


# Command-line execution
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please provide a subreddit to search.")
    else:
        top_ten(sys.argv[1])
