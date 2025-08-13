# SQL Translation
Currently (26-Feb-2023), following dialects are supported
- Teradata SQL
- AWS Redshift SQL
## Before you begin (prepare)
1. [collect_source_files](https://cloud.google.com/bigquery/docs/batch-sql-translator#collect_source_files)
  - Source files can also include comments
3. [create_metadata_files](https://cloud.google.com/bigquery/docs/batch-sql-translator#create_metadata_files)
  1. use `dwh-migration-dumper` command-line tool to [generate the metadata information](https://cloud.google.com/bigquery/docs/generate-metadata)
  2. Once metadata files are prepared, include them along with the source files in the translation source folder
  3. 

# Get Started
You have three options for submitting a batch translation job:
## CLI: [Batch translation client](https://github.com/google/dwh-migration-tools)
Configure a job by changing settings in a configuration file, and submit the job using the command line. This approach doesn't require you to 

- an open-source Python client
- allows you to translate source files located on your local machine, and have the translated files output to a local directory. 
- It still uses Cloud Storage to store files during translation job processing, but no manually upload source files to Cloud Storage. 
- If you choose to, you can also configure the client to address more complex tasks 
  - macro replacement
  - pre- and postprocessing of translation inputs and outputs. 

## Interactive :Google Cloud console
Configure and submit a job using a user interface. 
- requires you to upload source files to Cloud Storage.
## BigQuery Migration API
Configure and submit a job programmatically. 
- requires you to upload source files to Cloud Storage.
- [Client Libraries](https://cloud.google.com/bigquery/docs/reference/migration) support Go, Python, Java (no javascript)
## Limit
- Each individual source and metadata file can be up to 10 MB
- The total size of all input files(including source files and metadata files) uploaded to Cloud Storage can be up to 1 GB
- up to 25 other Migration API requests (create/start workflow) per minute, per project




