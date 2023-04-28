[wiki](https://github.com/davidkhala/gcp-collections/wiki/Compute)


# Scheduler 实例时间表
> Compute Engine System service account service-<number>@compute-system.iam.gserviceaccount.com needs to have [compute.instances.stop] permissions applied in order to perform this operation.
- [Resolution](https://serverfault.com/questions/1073163/compute-engine-system-service-account-service-permissions-issue)

  
# Access  
## Use your own SSH key to instance
If adding key like 
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCI8w/vxh7NOolYz+ss7FF+/yU9XQjVHMUOzs6krF6zwlWjVv8IvpZK6u9Q2Gwe+Is5q8DJHnIGBGCCqMOgsovD1FwCwSBLzaf4iT0Tu5P1GsdUxWL56PRz31UIYDvldz4aFyh0J9cRgtpSYzs1Ir1GtftmgG0pJc9CaobuCb8Q58FkyNAE5pP+G3biiUwQG+zrhKjC57yqUeLQKGyrpTnlgXThFIQa41PbDtXcqNpILFg8NKT1KT8rMTvJIKcP+0S21/iL6ue3B000Wjtnw9gSXG7fptcdEVeKnAmbE/qWczjU/mPeAw+0oVCN1ev8ND3dgeOdY82szglXT3lJLdC3 ssh-key-2020-12-20
```
Then the user name for ssh login is `ssh-key-2020-12-20` than `ubuntu`
You can check this in instace Details -- SSH Keys
![image](https://user-images.githubusercontent.com/7227589/168241771-8a94556a-9243-43b2-b98a-cc746329fcea.png)
## Transfer files
`gcloud compute scp`
- [To Linux](https://cloud.google.com/compute/docs/instances/transfer-files)
- [To Windows](https://cloud.google.com/compute/docs/instances/transfer-files-windows)
