import unittest

from davidkhala.gcp.bq.migration.workflow import Workflow, SourceDialect
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
        workflow.location = "US" # TODO ?
        _id = workflow.create(gcs_source_path, gcs_target_path)
        print(_id)





if __name__ == "__main__":
    unittest.main()
