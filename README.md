# GCP Dataflow ETL Pipeline

A fully orchestrated ETL pipeline built with **Apache Airflow**, using **Google Cloud Dataflow** (Apache Beam) for transformation and **BigQuery** for storage. This project is designed to be deployed directly into an Airflow DAGs folder and executed via the Airflow web UI or scheduler.


## 📖 Description

This project implements a data pipeline for extracting, transforming, and loading (ETL) data using Google Cloud services. The pipeline logic is written using Apache Beam and executed through **Google Cloud Dataflow**, while orchestration is handled completely within **Apache Airflow**.

Once deployed into your Airflow environment, this pipeline can be triggered manually or scheduled to run periodically.

### Key Features

- ☁️ Cloud-native architecture: Airflow + Dataflow + BigQuery
- 🔄 Supports batch and streaming data ingestion (e.g., Datastream)
- 🧪 Beam-based transformation logic
- 🗓️ Fully managed and scheduled by Apache Airflow
- 📊 Final output written to BigQuery for analytics


## 📁 Project Structure
```
project-root/
├── dataflow_script.py     # Beam pipeline code (transform and load)
├── Datastream.py          # Custom source extractor or wrapper
├── airflow_dag.py         # Airflow DAG file to trigger the pipeline
└── README.md
```


⚙️ Requirements

In Airflow Environment
Apache Airflow 2.x

Google Cloud Provider package:

pip install apache-airflow-providers-google

Cloud Services
Google Cloud Project

Enabled APIs: BigQuery, Dataflow

IAM roles with permissions to launch Dataflow jobs and write to BigQuery

🚀 Deployment Steps
1. Copy the following files into your Airflow DAGs folder:

dataflow_script.py

Datastream.py

airflow_dag.py (your DAG definition)

2. Open the Airflow UI and confirm the DAG appears.

3. Trigger the DAG manually or set a schedule_interval for automatic runs.


