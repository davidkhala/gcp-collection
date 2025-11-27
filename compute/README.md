[wiki](https://github.com/davidkhala/gcp-collections/wiki/Compute)

Once you enable Compute Engine API, google will create a default service account named as
`<projectNumber>-compute@developer.gserviceaccount.com`
- project number can be found by `gcloud projects describe $project --format="value(projectNumber)"`
- It can be deleted by user. Once deleted, it cannot be re-created by re-enable Compute Engine API 

# Scheduler 实例时间表
> Compute Engine System service account service-<number>@compute-system.iam.gserviceaccount.com needs to have [compute.instances.stop] permissions applied in order to perform this operation.
- [Resolution](https://serverfault.com/questions/1073163/compute-engine-system-service-account-service-permissions-issue)

  
# Access  
## Use your own SSH key to instance
If adding key like 
```
ssh-rsa ... ssh-key-2020-12-20
```
Then the user name for ssh login is `ssh-key-2020-12-20` than `ubuntu`
You can check this in instace Details --> SSH Keys

## Transfer files
`gcloud compute scp`
- [To Linux](https://cloud.google.com/compute/docs/instances/transfer-files)
- [To Windows](https://cloud.google.com/compute/docs/instances/transfer-files-windows)
