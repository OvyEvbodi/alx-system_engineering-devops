#!/usr/bin/python3

"""Queries the Reddit API
and prints the titles of the first 10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """Queries the Reddit API
        and prints the titles of the first 10 hot posts for a given subreddit

    Args:
        subreddit(str): the subbreddit to query

    Returns:
        the titles of the first 10 hot posts for a given subreddit, if any,
        otherwise, None
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0\
               Safari/537.36'}

    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for item in data.get('data').get('children'):
            print(item.get('data').get('title'))

    else:
        print('None')
