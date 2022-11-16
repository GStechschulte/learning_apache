import datetime as dt
import pandas as pd
#from airflow import DAG
#from airflow.operators.bash import BashOperator
#from airflow.operators.python import PythonOperator
from airflow.decorators import task, dag

#from airflow.decorators.python import python_task

default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2017, 6, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}


# with DAG('airflow_tutorial_v01',
#          default_args=default_args, 
#          schedule='0 * * * *',
#          ) as dag:
    
#     def print_world():
#         print('world')

#     print_hello = BashOperator(task_id='print_hello', 
#                                bash_command='echo "hello"')
#     sleep = BashOperator(task_id='sleep',
#                          bash_command='sleep 5')
#     print_statement = PythonOperator(task_id='print_world',
#                                  python_callable=print_world)

# print_hello >> sleep >> print_statement

@dag('print_statements', default_args=default_args)
def printing():

    @task()
    def _print_world():
        print('hello world')
    
    @task()
    def _print_hey():
        print('hey gabriel')
    
    _print_world()
    _print_hey()

# no longer required to instantiate DAG into a global variable
printing()