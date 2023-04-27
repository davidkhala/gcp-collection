import unittest

from migrate.workflow import Workflow, SourceDialect

project_id = 'gcp-data-davidkhala'


class MigrateTestCase(unittest.TestCase):
    def test_on_davidkhala(self):
        # The Cloud Storage path for a directory of files to translate in a task.
        gcs_source_path = 'bq-migrate/1679986012789199394-2bqejsz713k7a/preprocessed'

        # The Cloud Storage path to write back the corresponding input files to.
        gcs_target_path = 'bq-migrate/1679986012789199394-2bqejsz713k7a/translated'

        workflow_name = 'demo-cust'
        workflow = Workflow(SourceDialect.Bteq, workflow_name)
        _id = workflow.create(gcs_source_path, gcs_target_path, project_id)
        print(_id)


if __name__ == '__main__':
    unittest.main()
