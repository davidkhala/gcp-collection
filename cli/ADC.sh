# Application Default Credentials (ADC) used in calling Google APIs.
# - used for local dev environment
setup() {
  # Interactive
  # no projectId if auth standalone, you can use `gcloud init` to add projectId into context
  gcloud auth application-default login
}
"$@"
