import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

REDDIT_SECRET = parser.get('reddit_api_keys', 'reddit_secret_key')
REDDIT_CLIENT_ID = parser.get('reddit_api_keys', 'reddit_client_id')

DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_NAME = parser.get('database', 'database_name')
DATABASE_PORT = parser.get('database', 'database_port')
DATABASE_USERNAME = parser.get('database', 'database_username')
DATABASE_PASSWORD = parser.get('database', 'database_password')

# aws_access_key_id = 
# aws_secret_access_key= 
# aws_session_token= [aws session token]
# azure_region = uksouth
AZURE_CONNECTION_STRING = parser.get('azure', 'azure_connection_string')
AZURE_STORAGE_ACCOUNT_NAME = parser.get('azure', 'azure_storage_account_name')
AZURE_CONTAINER_NAME = parser.get('azure', 'azure_container_name')

INPUT_PATH = parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path')

POST_FIELDS = (
    'id',
    'title',
    'selftext',
    'author',
    'num_comments',
    'created_utc',
    'over_18',
    'spoiler',
    'upvote_ratio'
)