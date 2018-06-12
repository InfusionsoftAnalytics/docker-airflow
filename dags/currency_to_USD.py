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
dag = DAG('currency_to_USD', default_args=default_args, schedule_interval='0 2,8,14,20 * * *')

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='currency_to_USD',
    bash_command='python3 /home/engineering/currency_to_USD/currency_to_USD.py',
    dag=dag)
