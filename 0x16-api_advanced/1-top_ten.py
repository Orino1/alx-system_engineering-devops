#!/usr/bin/python3
"""
A module for requesting top 10 posts via reddit api
"""

import requests


def top_ten(subreddit):
    """
    requesting top 10 posts via reddit api
    args:
        subreddit: string - subreddit name
    """

    url = f"https://www.reddit.com/r/{subreddit}/top.json?limit=10"
    headers = {'User-Agent': 'this is my agent'}
    params = {
        'limit': '10'
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        for ithem in children:
            print(ithem['data']['title'])
        return
    print('None')
