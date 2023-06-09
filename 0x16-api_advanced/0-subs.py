#!/usr/bin/python3
import requests

"""
Funtion to query subscribers of reddit
"""

def number_of_subscribers(subreddit):
    """
    nummber_of_subscribers - To get the number of subscription in a subreddit
    Args:
        subreddit(str) - A subreddit
    """
    if subreddit is None or isinstance(subreddit, str) is False:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    request = requests.get(url, headers={"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}, allow_redirects = False)

    if request.status_code == 404:
        return 0

    subs = request.json().get('data').get("subscribers")
    return subs
