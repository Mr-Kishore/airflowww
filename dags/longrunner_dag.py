from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import time
import logging

# DAG config
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'keep_alive_long_running_job',
    default_args=default_args,
    description='Simulates a long job with periodic heartbeats',
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
)

# Simulated long-running task
def long_running_job_with_heartbeat(**kwargs):
    logger = logging.getLogger("airflow.task")
    total_runtime = 60 * 15  # 15 minutes
    interval = 60            # Log heartbeat every 1 minute
    iterations = total_runtime // interval

    for i in range(iterations):
        logger.info(f"Heartbeat: iteration {i + 1} of {iterations}")
        # Simulate some work here by waiting
        time.sleep(interval)
    
    logger.info("Job finished successfully!")

long_task = PythonOperator(
    task_id='simulate_long_job',
    python_callable=long_running_job_with_heartbeat,
    provide_context=True,
    dag=dag,
)
