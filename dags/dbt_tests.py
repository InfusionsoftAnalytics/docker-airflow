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

dag = DAG('dbt_tests', default_args=default_args, schedule_interval='0 0 * * *')

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='look_comparison_test',
    bash_command='python3 /home/engineering/dbt/tests/test_looks_between_branches.py',
    dag=dag)