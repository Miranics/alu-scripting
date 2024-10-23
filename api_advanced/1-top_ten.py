#!/usr/bin/python3
import requests

def top_ten(subreddit):
    # Define the user-agent to avoid request denial
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Define the URL for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    
    # Make a GET request to Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the status code indicates a valid response
    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        # Print the titles of the first 10 hot posts
        for post in data:
            print(post.get('data', {}).get('title'))
    else:
        print(None)
