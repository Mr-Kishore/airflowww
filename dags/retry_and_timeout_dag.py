from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
import random
import time

default_args = {
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': timedelta(seconds=10),
    'execution_timeout': timedelta(seconds=30)
}

def simulate_task():
    """Simulates a task that randomly succeeds or fails."""
    time.sleep(5)  # Simulate some processing time
    if random.choice([True, False]):
        print("✅ Task succeeded.")
    else:
        raise Exception("❌ Task failed.")

def decide_next_step(**context):
    """Decides which path to take based on previous task result."""
    ti = context['ti']
    task_status = ti.xcom_pull(task_ids='process_data')
    if task_status is None:
        return 'handle_failure'
    else:
        return 'handle_success'

def handle_success():
    print("🎉 Workflow completed successfully!")

def handle_failure():
    print("🚨 Workflow failed after retries.")

with DAG(
    dag_id='retriable_task_with_branching',
    default_args=default_args,
    description='A DAG with retry, timeout, and branching logic using Python',
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['retry', 'timeout', 'branch']
) as dag:

    run_main_task = PythonOperator(
        task_id='process_data',
        python_callable=simulate_task
    )

    choose_path = BranchPythonOperator(
        task_id='evaluate_result',
        python_callable=decide_next_step,
        provide_context=True
    )

    success_task = PythonOperator(
        task_id='handle_success',
        python_callable=handle_success
    )

    failure_task = PythonOperator(
        task_id='handle_failure',
        python_callable=handle_failure
    )

    end = EmptyOperator(task_id='end')

    run_main_task >> choose_path
    choose_path >> [success_task, failure_task]
    [success_task, failure_task] >> end

