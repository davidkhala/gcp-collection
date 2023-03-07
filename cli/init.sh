enableServices() {
  gcloud services enable bigquery.googleapis.com \
    bigquerydatatransfer.googleapis.com \
    cloudkms.googleapis.com \
    compute.googleapis.com \
    container.googleapis.com \
    dns.googleapis.com \
    iam.googleapis.com \
    logging.googleapis.com \
    monitoring.googleapis.com \
    redis.googleapis.com \
    sqladmin.googleapis.com
}
$@
