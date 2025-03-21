import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from pipelines.reddit_pipeline import reddit_pipeline

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args = {
    'owner': 'Kevin',
    'start_date': datetime(2025,3,18)
}

file_postfix = datetime.now().strftime('%Y%m%d')

dag = DAG(
    dag_id='etl_reddit_pipeline',
    schedule_interval='@daily',
    default_args=default_args,
    catchup=False
)

# Extract data from reddit
extract = PythonOperator(
    task_id='reddit_data_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    }
)