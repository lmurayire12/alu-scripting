#!/usr/bin/python3
""" 2-recurse.py """
import praw

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET', user_agent='YOUR_USER_AGENT')
    try:
        subreddit_info = reddit.subreddit(subreddit)
    except praw.exceptions.Redirect:
        return None
    if not subreddit_info.exists():
        return None
    hot_posts = subreddit_info.hot(limit=100, after=after)
    for post in hot_posts:
        hot_list.append(post.title)
    if len(hot_posts) == 100:
        return recurse(subreddit, hot_list, after=hot_posts[-1].name)
    else:
        return hot_list
