#!/usr/bin/python3
"""
This is a function that queries subscribers on a given subreddit on Reddit.
"""

import requests


def number_of_subscribers(subreddit):
    '''
    Queries the Reddit API and returns the number of subscribers
    '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0