import unittest

from davidkhala.gcp.bq.export import Export
from davidkhala.gcp.bq.migrate.workflow import Workflow, SourceDialect
from tests.ci import credential

project_id = "gcp-data-davidkhala"


class MigrateTestCase(unittest.TestCase):
    def test_on_davidkhala(self):
        # The Cloud Storage path for a directory of files to translate in a task.
        gcs_source_path = "bq-migrate/1679986012789199394-2bqejsz713k7a/preprocessed"

        # The Cloud Storage path to write back the corresponding input files to.
        gcs_target_path = "bq-migrate/1679986012789199394-2bqejsz713k7a/translated"

        workflow = Workflow(credential())
        workflow.name = "demo-cust"
        workflow.dialect = SourceDialect.Bteq
        workflow.project = project_id
        _id = workflow.create(gcs_source_path, gcs_target_path)
        print(_id)


class ExportTestCase(unittest.TestCase):
    table_id = "gcp-data-davidkhala.dbt_davidkhala.country_codes"

    def test_arrow(self):
        export = Export(credential())
        export.of(table_id=self.table_id)

        export.as_arrow()
        # TODO WIP gcs_target = "bq-migrate/country_codes"


if __name__ == "__main__":
    unittest.main()
