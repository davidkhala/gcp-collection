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
dataProject() {
  gcloud config set project gcp-data-davidkhala
}
freeProject() {
  gcloud config set project freetier-only
}

desktop(){
  # Interactive
  gcloud init
}

server() {
  # Interactive
  gcloud init --no-browser
}
"$@"
