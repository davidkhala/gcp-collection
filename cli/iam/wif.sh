# Workload Identity Federation (wif)
set -e
# ref: https://github.com/marketplace/actions/authenticate-to-google-cloud#indirect-wif
create-pool() {
    local name="${1}"
    gcloud iam workload-identity-pools create $name --location="global"
    gcloud iam workload-identity-pools describe $name --location="global" --format="value(name)" # The returned value
}
delete-pool() {
    local name="${1}"
    # This is a soft delete. It will be marked as Deleted but retained for 30 days
    # There's no supported way to force a hard delete
    gcloud iam workload-identity-pools delete $name --location="global"
}

setup-github-action() {
    local pool="${1}"
    local provider="${2}"
    local service_account="${3:-"cloud-region@freetier-only.iam.gserviceaccount.com"}"
    local GITHUB_ORG="${3:-davidkhala}"
    poolId=$(create-pool $pool)

    gcloud iam workload-identity-pools providers create-oidc $provider --location="global" --workload-identity-pool=$pool \
        --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository,attribute.repository_owner=assertion.repository_owner" \
        --attribute-condition="assertion.repository_owner == '${GITHUB_ORG}'" --issuer-uri="https://token.actions.githubusercontent.com"

    gcloud iam service-accounts add-iam-policy-binding $service_account --role="roles/iam.workloadIdentityUser" --member="principalSet://iam.googleapis.com/$poolId/attribute.repository_owner/$GITHUB_ORG"

    gcloud iam workload-identity-pools providers describe $provider --location="global" --workload-identity-pool=$pool --format="value(name)"
}
"$@"
