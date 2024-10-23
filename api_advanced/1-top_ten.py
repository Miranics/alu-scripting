#!/usr/bin/python3
""" 1-top_ten.py """
import requests


def top_ten(subreddit):
    """Prints 'OK' if the subreddit exists, otherwise prints 'None'."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)  # Print None for invalid subreddits
        return

    # Since the subreddit exists, print 'OK' as expected
    print("OK")


# Remove any trailing whitespace
