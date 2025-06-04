import airflow
from airflow import DAG
from datetime import timedelta
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from google.cloud import storage
import requests
import tempfile
import csv
from airflow.providers.google.cloud.operators.dataflow import DataflowCreatePythonJobOperator


default_args = {
    'start_date': airflow.utils.dates.days_ago(0),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'DataStream',
    default_args=default_args,
    description='Data-Flow Project',
    schedule_interval='@daily',
    max_active_runs=2,
    catchup=False,
    dagrun_timeout=timedelta(minutes=10),
)

Dummy_task = DummyOperator(
	task_id='Dummy_task', 
	dag=dag
)


def fetch_and_upload():
	url = "https://youtube138.p.rapidapi.com/v2/trending"

	headers = {
		"x-rapidapi-key": "aa31a53a62msh513f1a022780c99p16c578jsn93c92a95573a",
		"x-rapidapi-host": "youtube138.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers)

	if response.status_code == 200:
			data = response.json().get('list', [])
			if not data:
				print("No data received from API.")
				return
			
			# Temporary file for storing data before Loading to GCS
			with tempfile.NamedTemporaryFile(mode='w', delete=False, newline='', encoding='utf-8') as temp_file:
				writer = csv.DictWriter(temp_file, fieldnames=['title', 'author', 'authorurl','viewcount'])
				for entry in data:
					writer.writerow({field: entry.get(field) for field in ['title', 'author', 'authorurl','viewcount']})
				
				temp_file_path = temp_file.name    

			 # Upload to GCS
			client = storage.Client()
			bucket = client.get_bucket('ytdtstreaming')
			blob = bucket.blob('Youtube-ranking.csv')
			blob.upload_from_filename(temp_file_path)
			print("File successfully uploaded to GCS.")	
			
			
	else:
				print("API request failed:", response.status_code)
			
extract_and_upload_task = PythonOperator(
    task_id='fetch_and_upload',
    python_callable=fetch_and_upload,
	dag=dag
)

dataflow_task = DataflowCreatePythonJobOperator(
    task_id="dataflow_python_job",
    dataflow_default_options={
        "temp_location": "gs://df-demo10/temp",
        "location": "us-central1",
        "project": "hidden-bond-450621-a6",
        "region": "us-central1",
		"requirementss_file": "gs://ytdtstreaming/Data_flow/requirements.txt"
       
    },
    py_file="gs://ytdtstreaming/Data_flow/dataflow_script.py",
    dag=dag
)


Dummy_task >> extract_and_upload_task >> dataflow_task