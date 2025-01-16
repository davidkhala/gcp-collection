# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.cloud import bigquery_migration_v2

from davidkhala.gcp.bq import BigQuery

from davidkhala.gcp.bq.migrate import SourceDialect


class Workflow(BigQuery):
    name: str
    dialect: SourceDialect

    def create(self, gcs_input_path: str, gcs_output_path: str) -> str:
        """
        Creates a migration workflow of a Batch SQL Translation and return the id.
        TODO make this generic from BTEQ
        """
        parent = f"projects/{self.project_id}/locations/{self.location}"

        # Construct a BigQuery Migration client object.
        client = bigquery_migration_v2.MigrationServiceClient()

        # Set the source dialect to Teradata SQL.
        source_dialect = bigquery_migration_v2.Dialect()

        # always use BTEQ mode (which includes SQL).
        source_dialect.teradata_dialect = bigquery_migration_v2.TeradataDialect(
            mode=bigquery_migration_v2.TeradataDialect.Mode.BTEQ
        )

        # Set the target dialect to BigQuery dialect.
        target_dialect = bigquery_migration_v2.Dialect()
        target_dialect.bigquery_dialect = bigquery_migration_v2.BigQueryDialect()

        # Prepare the config proto.
        translation_config = bigquery_migration_v2.TranslationConfigDetails(
            gcs_source_path="gs://" + gcs_input_path,
            gcs_target_path="gs://" + gcs_output_path,
            source_dialect=source_dialect,
            target_dialect=target_dialect,
        )

        # Prepare the task.
        migration_task = bigquery_migration_v2.MigrationTask(
            type_=f"Translation_{self.dialect.value}2BQ",
            translation_config_details=translation_config,
        )

        # Prepare the workflow.
        workflow = bigquery_migration_v2.MigrationWorkflow(display_name=self.name)

        workflow.tasks["translation-task"] = migration_task  # type: ignore

        # Prepare the API request to create a migration workflow.
        request = bigquery_migration_v2.CreateMigrationWorkflowRequest(
            parent=parent,
            migration_workflow=workflow,
        )

        _migrationWorkflow = client.create_migration_workflow(request=request)

        return _migrationWorkflow.name
