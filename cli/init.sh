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
