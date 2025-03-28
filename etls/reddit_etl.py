import sys
import pandas as pd
import numpy as np
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

def extract_post(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)
    post_list = []
    for post in posts:
        post_dict = vars(post)
        post = {field: post_dict[field] for field in POST_FIELDS}
        post_list.append(post)

    return post_list

def transform_data(postdf: pd.DataFrame):
    postdf['id'] = postdf['id'].astype(str)
    postdf['title'] = postdf['title'].astype(str)
    postdf['selftext'] = postdf['selftext'].astype(str)
    postdf['author'] = postdf['author'].astype(str)
    postdf['num_comments'] = postdf['num_comments'].astype(int)
    postdf['created_utc'] = pd.to_datetime(postdf['created_utc'], unit='s')
    postdf['over_18'] = np.where(
        (postdf['over_18'] == False) | (postdf['over_18'] == 'False'), False, True
    ).astype(bool)
    postdf['spoiler'] = np.where(
        (postdf['spoiler'] == False) | (postdf['spoiler'] == 'False'), False, True
    ).astype(bool)
    postdf['upvote_ratio'] = postdf['upvote_ratio'].astype(float)
    return postdf

def export_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path, index=False)