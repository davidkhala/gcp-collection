# HA
- cross-region replication: by Secondary Cluster (preview)
- RTO follows [CloudSQL](https://services.google.com/fh/files/misc/resiliency_with_cloud_sql_whitepaper.pdf
  - RTO = 1 minute for Instance Failure
  - RTO = several minutes for Zone Failure
- Primary instance Failover: 2 minutes 
## Secondary Cluster
A read-only cluster in a different region than the primary, that replicates from the primary cluster asynchronously
- In the event of a failure of an AlloyDB primary cluster, you can promote a secondary cluster to a primary cluster.
- It cannot be in the same region as primary instance

## Provision time
- Cluster with 1 primary instance:  15 minutes
- Add new Read pool instance (NodeCount=1, after cluster provision): 8 minutes
# Backup
- backup is always a full backup
- Backup and restore are managed entirely by AlloyDB's storage layer. No impact on the read and write performance 

## Continuous backup and recovery
AlloyDB lets you restore an existing cluster to any moment from its recent history, with microsecond granularity.
- Retention period: AlloyDB lets you choose any point in time up to 1-35 days into the past. Default 14 days
- Creates one backup every day by default
- Target: the same cluster or a new cloned copy of cluster
- make AlloyDB **RPO=0**

## On-demand, scheduled backup
- Retention period: up to one year

# Dump
by `pg_dump`
