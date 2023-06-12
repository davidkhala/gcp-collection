# Dataflow
## Usage
Dataflow usage is billed in per second increments, on a per job basis.
Usage is stated in hours in order to apply hourly pricing to second-by-second use.


# Dataflow Prime
Charge unit: Data Compute Units (DCUs) (batch and streaming)
- Resources tracked by DCUs include vCPU, memory, Dataflow Shuffle data processed (for batch jobs), and Streaming Engine data processed (for streaming jobs).
- One DCU = 1 vCPU 4 GB worker / hour / dataflow job.
- You can't set the number of DCUs for your jobs. DCUs are counted by Dataflow Prime in serverless way. 

Hongkong DC price
| Job Type | Data Compute Units (per DCU) |
| -------- | ---------------------------- |
| Batch    | $0.084                       |
| Streaming| $0.125                       |




