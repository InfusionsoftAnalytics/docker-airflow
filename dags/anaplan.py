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
    'start_date': datetime(2018, 5, 1),
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
dag = DAG('anaplan', default_args=default_args, schedule_interval='0 * * * *')

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='fetch_data_from_NetSuite',
    bash_command='source /home/engineering/anaplan/ODBCDrivers/oaodbc64.sh && python3 /home/engineering/anaplan/fetch_from_netsuite.py',
    dag=dag)

t2 = BashOperator(
    task_id='run_queries_from_BQ',
    bash_command='python3 /home/engineering/anaplan/run_queries_from_BQ.py',
    dag=dag)

t3 = BashOperator(
    task_id='push_to_Anaplan',
    bash_command='python3 /home/engineering/anaplan/push_to_anaplan.py',
    dag=dag)

t2.set_upstream(t1)
t3.set_upstream(t2)
