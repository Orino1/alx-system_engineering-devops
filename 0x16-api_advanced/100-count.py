#!/usr/bin/python3
"""
A module for requesting all hot titles recursively and printing
all key-words count
"""


import requests


def count_words(subreddit, word_list, wc={}, last_title='', wh=0):
    """
    a recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    """
    url = f'https://reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'this is my agent'}
    params = '?after='
    title = ''
    if last_title != '':
        url = url + params + last_title
    else:
        for item in word_list:
            wc[item.lower()] = 0
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        for child in children:
            title = child['data']['title']
            for item in word_list:
                wc[item.lower()] += title.lower().count(item.lower())
        last_title = children[-1]['data']['title']
        count_words(subreddit, word_list, last_title=title, wh=wh+1)
        if wh == 0:
            # this line is from stackoverflow
            sorted_items = sorted(wc.items(), key=lambda x: (-x[1], x[0]))
            for keyword, count in sorted_items:
                if count > 0:
                    print(f"{keyword}: {count}")
        else:
            wh -= 1
            return
    else:
        wh -= 1
        return
