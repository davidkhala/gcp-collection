# Application Default Credentials (ADC) used in calling Google APIs.
# - used for local dev environment
set -e
setup() {
  gcloud auth application-default login # Interactive
  project=$(gcloud config get-value project)
  if [ -z "$project" ]; then
    echo "set project $1"
    set-project $1
  fi

}
access-token() {
  gcloud auth application-default print-access-token
}
set-project() {
  gcloud auth application-default set-quota-project $1
  gcloud config set project $1
}
logout() {
  gcloud auth application-default revoke
}
"$@"
