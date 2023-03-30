# [time-travel](https://cloud.google.com/bigquery/docs/time-travel)
Time travel lets you 
- query data that was updated or deleted
- restore a table that was deleted
- restore a table that expired.

[configure_the_time_travel_window](https://cloud.google.com/bigquery/docs/time-travel#configure_the_time_travel_window)
- from 2 days up to 7 days
- default to 7 days

## query
GoogleSQL sample
```
SELECT * FROM `mydataset.mytable`
  FOR SYSTEM_TIME AS OF TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR);
```

Legacy SQL sample
```
SELECT COUNT(*) FROM [PROJECT_ID:DATASET.TABLE@-3600000]
```
## Restore table
```
bq cp mydataset.table1@-3600000 mydataset.table1_restored
```

# Limit
- Travel window up to 7 days
- Query cannot refer to an external table
