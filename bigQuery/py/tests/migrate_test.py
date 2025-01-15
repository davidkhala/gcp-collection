import unittest

from davidkhala.gcp.bq.export import Export
from davidkhala.gcp.bq.migrate.workflow import Workflow, SourceDialect
from tests.ci import credential

project_id = 'gcp-data-davidkhala'
datasets = ['dbt_davidkhala', 'translate']


class MigrateTestCase(unittest.TestCase):
    def test_on_davidkhala(self):
        # The Cloud Storage path for a directory of files to translate in a task.
        gcs_source_path = 'bq-migrate/1679986012789199394-2bqejsz713k7a/preprocessed'

        # The Cloud Storage path to write back the corresponding input files to.
        gcs_target_path = 'bq-migrate/1679986012789199394-2bqejsz713k7a/translated'

        workflow_name = 'demo-cust'
        workflow = Workflow(SourceDialect.Bteq, workflow_name, project_id)
        _id = workflow.create(gcs_source_path, gcs_target_path)
        print(_id)


class ExportTestCase(unittest.TestCase):
    def test_dbt(self):
        export = Export(credential())
        export.of(table_id='gcp-data-davidkhala.dbt_davidkhala.country_codes')

        export.as_arrow()
        gcs_target = 'bq-migrate/country_codes'
        export.print()



if __name__ == '__main__':
    unittest.main()
