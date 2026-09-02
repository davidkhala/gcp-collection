dataProject() {
  gcloud config set project gcp-data-davidkhala
}
baseProject() {
  gcloud config set project gcp-base-davidkhala
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
