import unittest
from migrate.create_migration_workflow import create_migration_workflow

project_id = 'gcp-data-davidkhala'


class MigrateTestCase(unittest.TestCase):
    def test_on_davidkhala(self):
        # The Cloud Storage path for a directory of files to translate in a task.
        gcs_source_path = 'bq-migrate/1679986012789199394-2bqejsz713k7a/preprocessed'

        # The Cloud Storage path to write back the corresponding input files to.
        gcs_target_path = 'bq-migrate/1679986012789199394-2bqejsz713k7a/translated'

        workflow_name = 'demo-cust'
        create_migration_workflow(gcs_source_path, gcs_target_path, project_id, workflow_name)


if __name__ == '__main__':
    unittest.main()
