# DR


## Backup
- You can't export a backup. You can only export instance data. 
### Automated backups
- Automated backups are taken daily
- One additional automated backup is taken after your instance is stopped (to safeguard all changes prior to the instance stopping)
- 1-365 backups are retained, 7 by default.

## export to GCS (object storage)
- [pg_dump: postgre native tool](https://cloud.google.com/sql/docs/postgres/import-export/import-export-dmp)
- [SQL dump](https://cloud.google.com/sql/docs/postgres/import-export/import-export-sql#export-sql-dump-file)
