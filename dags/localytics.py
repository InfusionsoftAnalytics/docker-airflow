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
    'start_date': datetime(2018, 3, 19),
    'email': ['daniel.francis@infusionsoft.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
}

dag = DAG('localytics', default_args=default_args, schedule_interval='0 */4 * * *')

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='get_user_data',
    bash_command='python3 /home/engineering/localytics/localytics_user_data.py',
    dag=dag)

t2 = BashOperator(
    task_id='get_aggregates',
    bash_command='python3 /home/engineering/localytics/localytics_aggregates.py',
    dag=dag)

