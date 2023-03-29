
setup() {
  gcloud init
}
loginWebUser(){
  gcloud auth login --brief
}
setupADC() {
  # Application Default Credentials (ADC) used in calling Google APIs. 
  # used for local dev environment to use lanuage specific gcp sdk 
  # no projectId if auth standalone, you can use `gcloud init` to add projectId into context
  gcloud auth application-default login
}
setupServer() {
  gcloud init --no-browser
}
setServiceAccount() {
  gcloud auth activate-service-account --key-file=$1
}
logout() {
  gcloud auth revoke
  gcloud auth application-default revoke
}
list() {
  gcloud auth list # not showing application-default credential

  gcloud auth application-default print-access-token
}
$@
