install() {
  sudo tee -a /etc/yum.repos.d/google-cloud-sdk.repo <<EOM
[google-cloud-cli]
name=Google Cloud CLI
baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el8-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=0
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOM

  sudo dnf install -y google-cloud-cli

}
setup() {
  gcloud init
}
setup-server() {
  gcloud init --no-browser
}
setup-service-account() {
  gcloud auth activate-service-account --key-file=$1
}
logout() {
  gcloud auth revoke
}
$@
