#!/usr/bin/python3
"""
get top 10 hot posts function
"""

import json
import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a subreddit."""
    if len(sys.argv) < 2:
        print(None)
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {"User-Agent": "Mozilla/5.0"}
        result = requests.get(url, headers=headers, allow_redirects=False)
        if result.status_code != 200:
            print(None)
        else:
            data = json.loads(result.text)["data"]["children"]
            for post in data[:10]:
                print(post["data"]["title"])
                