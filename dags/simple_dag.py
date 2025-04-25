from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def greet():
    print("Hello, Kishore! Airflow is running.")

with DAG(
    dag_id="simple_dag",
    start_date=datetime(2025, 4, 1),
    schedule_interval=None,
    catchup=False,
) as dag:
    task = PythonOperator(
        task_id="my_task",
        python_callable=greet )
