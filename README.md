# gcp-dataflow-etl-pipeline

A fully orchestrated ETL pipeline built with **Apache Airflow**, using **Google Cloud Dataflow** (Apache Beam) for transformation and **BigQuery** for storage. This project is designed to be deployed directly into an Airflow DAGs folder and executed via the Airflow web UI or scheduler.

---

## 📖 Description

This project implements a data pipeline for extracting, transforming, and loading (ETL) data using Google Cloud services. The pipeline logic is written using Apache Beam and executed through **Google Cloud Dataflow**, while orchestration is handled completely within **Apache Airflow**.

Once deployed into your Airflow environment, this pipeline can be triggered manually or scheduled to run periodically.

### Key Features

- ☁️ Cloud-native architecture: Airflow + Dataflow + BigQuery
- 🔄 Supports batch and streaming data ingestion (e.g., Datastream)
- 🧪 Beam-based transformation logic
- 🗓️ Fully managed and scheduled by Apache Airflow
- 📊 Final output written to BigQuery for analytics

---

## 📁 Project Structure

```text
project-root/
├── dataflow_script.py     # Beam pipeline code (transform and load)
├── Datastream.py          # Custom source extractor or wrapper
├── requirements.txt       # Python dependencies
└── README.md
```

---

## ⚙️ Requirements

### Python Packages

Install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Contents:
```
apache-beam[gcp]
google-cloud-bigquery
google-cloud-storage
```

### Google Cloud Setup

Make sure the following GCP APIs are enabled:
- Dataflow
- BigQuery
- Cloud Storage

And ensure your service account or user has appropriate IAM roles:
- Dataflow Admin
- BigQuery Data Editor
- Storage Admin

---

## 🚀 Deployment Steps

1. Copy the following files into your Airflow DAGs folder:
   - `dataflow_script.py`
   - `Datastream.py`
   - `requirements.txt`

2. Open the Airflow UI and confirm the DAG appears.

3. Trigger the DAG manually or configure a schedule interval.

> ⚠️ Note: DAG execution will launch a Dataflow job on GCP, so ensure all GCP configurations and credentials are properly set up in your Airflow environment.


