loginWebUser() {
  gcloud auth login --brief
}

loginServiceAccount() {
  # same as `gcloud auth login --cred-file=$1` while uses a service account
  gcloud auth activate-service-account --key-file=$1
}
logout() {
  gcloud auth revoke
}
listAccounts() {
  # lists credentialed accounts
  gcloud auth list
}
update() {
  gcloud components update -q
}
"$@"
