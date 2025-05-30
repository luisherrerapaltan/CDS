#!/bin/bash -l
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=genius
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --time=00:10:00
#SBATCH --output=slurm-%j.out

# (Optional) show where we are and when:
echo "Host: $(hostname)"
echo "Working dir: $(pwd)"
date

# Run your benchmark:
time python3 benchmark.py > bench_hpc.tsv

# Show the results in the Slurm output:
echo ""
echo "== bench_hpc.tsv =="
cat bench_hpc.tsv