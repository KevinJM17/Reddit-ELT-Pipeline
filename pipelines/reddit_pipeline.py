from utils.constants import REDDIT_SECRET, REDDIT_CLIENT_ID
from etls.reddit_etl import connect_reddit, extract_post

def reddit_pipeline(file_name:str, subreddit:str, time_filter='day', limit=None):
    instance = connect_reddit(REDDIT_SECRET, REDDIT_CLIENT_ID, 'subreddit scrapper')
    posts = extract_post(instance, subreddit, time_filter, limit)
    print(posts)
    # pass