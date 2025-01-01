loginWebUser() {
  gcloud auth login --brief
}

loginServiceAccount() {
  # same as `gcloud auth login --cred-file=$1` while uses a service account
  gcloud auth activate-service-account --key-file=$1
}
logout() {
  gcloud auth revoke
  gcloud auth application-default revoke
}
listAccounts() {
  # lists credentialed accounts
  gcloud auth list # not showing application-default credential

  gcloud auth application-default print-access-token
}
update() {
  gcloud components update -q
}
"$@"
