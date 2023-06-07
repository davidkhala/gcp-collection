// https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create
create-firewall() {
    local name=$1
    local allowList=${2:-tcp:80,icmp,tcp:22}
    local direction=${3:-INGRESS} # INGRESS | EGRESS
    gcloud compute firewall-rules create ${name} --allow=tcp:8080 --description="Allow ${direction} traffic on ${allowList}" --direction=${direction}
}
$@
