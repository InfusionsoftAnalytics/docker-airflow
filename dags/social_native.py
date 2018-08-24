"""
Code that goes along with the Airflow tutorial located at:
https://github.com/airbnb/airflow/blob/master/airflow/example_dags/tutorial.py
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
default_args = {
    'owner': 'Infusionsoft',
    'depends_on_past': False,
    'start_date': datetime(2018, 3, 1),
    'email': ['daniel.francis@infusionsoft.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}
dag = DAG('social_native', default_args=default_args, schedule_interval='0 */6 * * *')

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='get_facebook_native',
    bash_command='python3 /home/engineering/social_native/facebook_native/facebook_native.py',
    dag=dag)
t2 = BashOperator(
    task_id='get_instagram_native',
    bash_command='python3 /home/engineering/social_native/instagram_native/instagram_native.py',
    dag=dag)
t3 = BashOperator(
    task_id='get_linkedin_native',
    bash_command='python3 /home/engineering/social_native/linkedin_native/linkedin_native.py',
    dag=dag)
t4 = BashOperator(
    task_id='get_twitter_native',
    bash_command='python3 /home/engineering/social_native/twitter_native/twitter_native.py',
    dag=dag)
t5 = BashOperator(
    task_id='get_youtube_native',
    bash_command='python3 /home/engineering/social_native/youtube_native/youtube_native.py',
    dag=dag)
