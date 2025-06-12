# CDS
Concepts of Data Science - UHasselt 2024-2025
Students: Luis Cesar Herrera Paltan, Nele Verhulst

This repository contains documents for the project assignment about the implementation of a ternary research tree, for the CDS course at UHasselt 2024-2025. We implemented a ternary research tree and first did a local benchmark. Then we also benchmarked on the HPC infrastructure of the Vlaams Supercomputer Centrum (VSC). We collaborated on the project through this GitHub repository. 

These documents and folder are included in the repository:
- data folder: .txt files with lists of words used in the implementation and testing of the tree
- ternary_search_tree.py: Python module for TernarySearchTree
- ternary_search_tree.ipynb: Jupyter notebook that shows the implementation of the ternary search tree, the local benchmark and the results of the benchmark on the ternary search tree
- jobscript.slurm: job script used for benchmark on HPC infrastructure
- timings.txt: output of the benchmark runs on the HPC infrastructure
- README.md: explanation of the project, contents of repository, and summary of conclusions

Summary of conclusions:
We expected a complexity for the average case of insert and search of O(log n). Our benchmark timed how long it took to insert/search a constant and relatively low (20) number of words into trees of growing size. Therefore, we measured per-operation cost at a larger scale and as the number of words increased, the average depth (and so the time to reach a match or failure) grew logarithmically.
For the local benchmark, all insert and search times were very low and erratic, so we could not clearly establish a curve to verify this. Changing the code to record times from time.time_ns() to int(time.time() * 1e9) like we did on the HPC infrastructure benchmark (to accomodate the older Python version that was installed there) did not improve this, so we kept the original code. The benchmark on the HPC infrastructure resulted in a logarithmic curve of insert and search times, confirming the expected complexity of our implementation.
