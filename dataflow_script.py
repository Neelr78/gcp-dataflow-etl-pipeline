import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import csv

class ParseCSV(beam.DoFn):
    """Parses a CSV line into a dictionary for BigQuery."""
    def process(self, line):
        fields = next(csv.reader([line]))  
        yield {
            "title": fields[0],
            "author": fields[1],
            "authorurl": fields[2] if len(fields) > 2 else None,
            "viewcount": int(fields[3]) if len(fields) > 3 and fields[3].isdigit() else 0
 
        }

def run(argv=None):
    pipeline_options = PipelineOptions(argv, save_main_session=True, streaming=False)

    with beam.Pipeline(options=pipeline_options) as pipeline:
        table_schema = "title:STRING," \
        "author:STRING," \
        "authorurl:STRING," \
        "viewcount:INTEGER"

        (
            pipeline
            | 'Read CSV from GCS' >> beam.io.ReadFromText('gs://ytdtstreaming/Youtube-ranking.csv', skip_header_lines=1)
            | 'Parse CSV' >> beam.ParDo(ParseCSV())  # 
            | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
                table='hidden-bond-450621-a6:ytdtstreaming.ytdtstream',
                schema=table_schema,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,  #
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,  #
                custom_gcs_temp_location="gs://df-demo10/temp"
            )
        )

if __name__ == '__main__':
    run()
