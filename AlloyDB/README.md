- Provision time (RPO) 15 minutes
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
- 

