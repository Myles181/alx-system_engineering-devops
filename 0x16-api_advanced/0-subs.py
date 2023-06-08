#!/usr/bin/python3
import requests

"""
Funtion to query subscribers of reddit
"""

def number_of_subscribers(subreddit):

    if subreddit is None or isinstance(subreddit, str) is False:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    request = requests.get(url, headers={"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"})

    if request.status_code == 404:
        return 0

    subs = request.json().get('data').get("subscribers")
    return subs

numOfSub = number_of_subscribers('0-subs')
print(numOfSub)
