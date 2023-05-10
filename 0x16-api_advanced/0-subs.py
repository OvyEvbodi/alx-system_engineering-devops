#!/usr/bin/python3

"""Gets the number of subscribers for a specified subreddit,
by querying the Reddit API
"""

from requests import get


def number_of_subscribers(subreddit):
    """Gets the number of subscribers for a specified subreddit,
    by querying the Reddit API

    Args:
        subreddit(str): the subbreddit to get number of subscribers

    Returns:
        the number of subscribers, if subreddit is valid,
        otherwise, 0
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0\
               Safari/537.36'}

    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data').get('subscribers')
        return data

    return 0
