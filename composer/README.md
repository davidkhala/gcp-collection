# Cloud Composer
built on Apache Airflow
- Provision time: 20 mins
## weakness
- Cannot stop instance
  - Alternative solution: https://medium.com/condenastengineering/automating-a-cloud-composer-development-environment-590cb0f4d880
- code not recoverable: The deletion of Composer will clean-up the files in bucket <region-code>-composer-<generated-id>-bucket
		○ But the bucket itself remains


