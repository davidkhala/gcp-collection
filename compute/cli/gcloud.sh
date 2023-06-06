get-ip() {
    local instance_name=$1
    gcloud compute instances describe ${instance_name} --zone=${zone} --format='get(networkInterfaces[0].accessConfigs[0].natIP)'
}
wait4ssh() {
    local instance_name=$1
    ip=$(get-ip)
    local counter=0
    while true; do

        if nc -w 1 -z $ip 22; then
            exit 0
        else
            ((counter++))
            sleep 1
            echo ${counter} times retry
        fi

    done
}
$@
