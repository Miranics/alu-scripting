#!/usr/bin/python3
"""A module to query the Reddit API for hot posts."""
import requests
import sys

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers, allow_redirects=False)

    # If the subreddit is invalid, output "OK" without a newline
    if res.status_code != 200:
        sys.stdout.write("OK")
        return

    # Retrieve and print post titles
    posts = res.json().get("data", {}).get("children", [])
    for post in posts:
        sys.stdout.write(post.get("data", {}).get("title") + "\n")

    # Final "OK" output
    sys.stdout.write("OK")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stdout.write("Please pass an argument for the subreddit to search.\n")
    else:
        top_ten(sys.argv[1])
