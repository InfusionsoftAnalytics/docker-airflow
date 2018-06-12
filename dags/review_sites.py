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
    'start_date': datetime(2018, 5, 4),
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
dag = DAG('review_sites', default_args=default_args, schedule_interval='0 2,8,14,20 * * *')

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='parsehub',
    bash_command='python3 /home/engineering/review_sites/review_sites.py',
    dag=dag)

t2 = BashOperator(
    task_id='capterra',
    bash_command='python3 /home/engineering/review_sites/capterra.py',
    dag=dag)

t3 = BashOperator(
    task_id='g2crowd',
    bash_command='python3 /home/engineering/review_sites/g2crowd.py',
    dag=dag)