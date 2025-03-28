import pandas as pd

from utils.constants import REDDIT_SECRET, REDDIT_CLIENT_ID, OUTPUT_PATH
from etls.reddit_etl import connect_reddit, extract_post, transform_data, export_to_csv

def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    reddit_instance = connect_reddit(REDDIT_SECRET, REDDIT_CLIENT_ID, 'subreddit scrapper')
    extracted_posts = extract_post(reddit_instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(extracted_posts)
    post_df = transform_data(post_df)
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    export_to_csv(post_df, file_path)
    return file_path