import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.azure_pipeline import upload_azure_pipeline


default_args = {
    'owner': 'Kevin',
    'start_date': datetime(2025,3,18)
}

file_postfix = datetime.now().strftime('%Y%m%d')

dag = DAG(
    dag_id='reddit_etl_pipeline',
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
    },
    dag=dag
)

# Upload data to Azure
upload_blob = PythonOperator(
    task_id='azure_data_upload',
    python_callable=upload_azure_pipeline,
    dag=dag
)

extract >> upload_blob