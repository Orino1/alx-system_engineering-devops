#!/usr/bin/python3
"""
A module for requesting the subscribers count via reddit api
"""

import requests


def number_of_subscribers(subreddit):
    """
    requesting the subscribers count via reddit api
    args:
        subreddit: string - subreddit name
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'this is my agent'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    return 0
