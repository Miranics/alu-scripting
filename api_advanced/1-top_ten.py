#!/usr/bin/python3
'''
Defines function that prints the top ten posts of a subreddit
'''
import requests


def top_ten(subreddit):
    '''Prints the top ten posts of a subreddit

    Return:
        None -  if the subreddit is invalid
    '''
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
    endpoint = 'https://www.reddit.com'
    headers = {'user-agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/shobi_ola)'}
    params = {'limit': 10}
    info = requests.get('{}/r/{}/hot.json'.format(endpoint, subreddit),
                        allow_redirects=False,
                        headers=headers,
                        params=params)
    if info.status_code == 200:
        json_info = info.json()
        for post in json_info.get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
        