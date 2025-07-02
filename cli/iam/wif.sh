# Workload Identity Federation (wif)
# TODO organize https://github.com/marketplace/actions/authenticate-to-google-cloud#indirect-wif
create-pool(){
    local name="${1}"
    gcloud iam workload-identity-pools create $name --project="${PROJECT_ID}" --location="global" --display-name="GitHub Actions Pool"
}
delete-pool(){
    local name="${1}"
    gcloud iam workload-identity-pools delete $name --location="global"
}
$@
