#!/usr/bin/python3

"""Queries the Reddit API
and prints the titles of the hot posts listed for a given subreddit
"""

from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API
        and prints the titles of the hot posts for a given subreddit

    Args:
        subreddit(str): the subbreddit to query
        hot_list: A list of titles of hot post

    Returns:
        the titles of hot posts for a given subreddit, if any,
        otherwise, None
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0\
               Safari/537.36'}
    params = {'after': after}

    response = get(url, headers=headers, allow_redirects=False, params=params)

    if response.status_code == 200:
        after = response.json().get('data').get('after', None)

        if after:
            return recurse(subreddit, hot_list, after)
        data = response.json()
        titles = data.get('data').get('children')
        for item in titles:
            hot_list.append(item.get('data').get('title'))

        return hot_list

    return None
