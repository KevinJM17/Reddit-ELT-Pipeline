import sys
from praw import Reddit

from utils.constants import POST_FIELDS

def connect_reddit(client_secret, client_id, user_agent) -> Reddit:
    try:
        reddit = Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
        print('Connected to Reddit.')
        return reddit

    except Exception as e:
        print(e)
        sys.exit(1)

def extract_post(reddit_instance:Reddit, subreddit:str, time_filter:str, limit=None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)
    post_list = []
    for post in posts:
        post_dict = vars(post)
        post = {field: post_dict[field] for field in POST_FIELDS}
        post_list.append(post)

    return post_list