#!/usr/bin/python3
"""
A module for requesting top 10 posts via reddit api
"""

import requests


def recurse(subreddit, hot_list=[], last_title=''):
    """
    Using recursive funtion to return a list of all hot titles
    args:
        subreddit: string - subreddit name
        hot_list: list - fill the list and return it
    """
    url = f'https://reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'this is my agent'}
    params = '?after='
    title = ''
    if last_title != '':
        url = url + params + last_title
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        for item in children:
            hot_list.append(item['data']['title'])
        title = children[-1]['data']['title']
        recurse(subreddit, last_title=title)
        return hot_list
    else:
        return
