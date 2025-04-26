from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from datetime import datetime
import subprocess

def run_script():
    script_path = "*your directory*/abc.py"
    result = subprocess.run(["python3", script_path], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Script failed: {result.stderr}")
    return result.stdout

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 19),
    'email_on_failure': False,
    'email_on_retry': False
}

with DAG(
    dag_id="run_external_python_script_with_email",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description="Runs external script and sends email notification",
    tags=["email", "script"],
) as dag:

    run_external_script = PythonOperator(
        task_id="run_script",
        python_callable=run_script,
    )

    send_email = EmailOperator(
        task_id="send_email",
        to="youremail@email.com",
        subject="✅ External Script Executed Successfully",
        html_content="<p>The external Python script has completed successfully.</p>",
        conn_id="f61b398ea26e",  # Make sure this matches the Airflow connection ID
    )

    run_external_script >> send_email
