enableServices() {
  gcloud services enable cloudkms.googleapis.com \
    compute.googleapis.com \
    dns.googleapis.com \
    iam.googleapis.com \
    logging.googleapis.com \
    monitoring.googleapis.com
}
dataProject() {
  gcloud config set project gcp-data-davidkhala
}
freeProject() {
  gcloud config set project freetier-only
}

desktop() {
  # Interactive
  gcloud init
}

server() {
  # Interactive
  gcloud init --no-browser
}
"$@"
