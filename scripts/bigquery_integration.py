from google.cloud import bigquery

def upload_to_bigquery(dataset_name, table_name, csv_file):
    client = bigquery.Client()

    dataset_ref = client.dataset(dataset_name)
    table_ref = dataset_ref.table(table_name)

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
    )

    with open(csv_file, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

    job.result()  # Wait for the job to complete.
    print(f"Loaded {job.output_rows} rows into {dataset_name}:{table_name}.")

if __name__ == "__main__":
    upload_to_bigquery("flight_data_dataset", "flight_data_table", "/data/historical_flight_data.csv")
