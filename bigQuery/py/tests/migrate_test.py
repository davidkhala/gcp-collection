import unittest

from davidkhala.gcp.bq.migrate.export import Export
from migrate.workflow import Workflow, SourceDialect

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
        export = Export(datasets[0], project_id)
        table = 'country_codes'
        columns = ['country_code', 'country_name']
        export.from_table(table, columns, '')
        gcs_target = 'bq-migrate/country_codes'
        export.print()



if __name__ == '__main__':
    unittest.main()
