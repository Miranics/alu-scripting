#!/usr/bin/python3
"""A module to query the Reddit API for hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Send a GET request to the subreddit URL
    res = requests.get(
        url, headers={"User-Agent": "Mozilla/5.0"}, allow_redirects=False
    )

    # Parse the JSON response
    if res.status_code == 200:
        json_response = res.json()
        posts = json_response.get("data", {}).get("children", [])

        # Print the titles of the first 10 hot posts
        for post in posts:
            print(post.get("data", {}).get("title"))

    # Print OK only once
    print("OK", end="")  # Print OK without a newline


# Test the function with the learnpython subreddit
top_ten("learnpython")
