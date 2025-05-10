# Getting Started with HyQCOpt

## 1. Installation
```bash
pip install hyqcopt
# For quantum backends
pip install hyqcopt[qiskit]
```
## 2. Solve a Problem
```python
from hyqcopt import create_solver
from hyqcopt.problems import TSP

# Create problem instance
distance_matrix = [[0, 2, 3], [2, 0, 1], [3, 1, 0]]
problem = TSP(distance_matrix)

# Initialize hybrid solver
solver = create_solver('qaoa', backend='qiskit')

# Solve and get results
result = solver.solve(problem)
print(f"Optimal route: {result.solution}")
```
## 3. Advanced Usage
```python
# Distributed solving
with distributed_session(executor='dask'):
    solver = create_solver('grover', workers=4)
    result = solver.solve(large_problem)

# Real-time monitoring
solver.attach_monitor(lambda x: print(f"Current energy: {x.energy}"))
```