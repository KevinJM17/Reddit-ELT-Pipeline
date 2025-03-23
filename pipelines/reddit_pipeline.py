from utils.constants import REDDIT_SECRET, REDDIT_CLIENT_ID

def reddit_pipeline(file_name:str, subreddit:str, time_filter='day', limit=None):
    instance = connect_reddit(REDDIT_SECRET, REDDIT_CLIENT_ID)
    pass