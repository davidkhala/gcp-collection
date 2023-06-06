get-ip() {
    local instance_name=$1
    gcloud compute instances describe ${instance_name} --zone=${zone} --format='get(networkInterfaces[0].accessConfigs[0].natIP)'
}

wait4ssh() {
    local instance_name=$1
    
    local counter=0
    while true; do
        if gcloud compute ssh ${instance_name} --zone=${zone} --quiet --command="true" 2> /dev/null; then
            exit 0
        else
            ((counter++))
            sleep 1
            echo ${counter} times retry
        fi

    done
}
delete-vm() {
    local instance_name=$1
    gcloud compute instances delete ${instance_name} --zone=${zone} --quiet
}

$@
