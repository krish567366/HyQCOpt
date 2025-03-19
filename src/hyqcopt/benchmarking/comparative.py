import time
from typing import Dict, List, Callable
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from hyqcopt.core.interfaces import OptimizationProblem, HybridSolver, QuantumBackend
from hyqcopt.classical.optimizers import ClassicalOptimizer
from hyqcopt.algorithms.grover import GroverOptimizer


class Benchmark:
    def __init__(self, metrics: Dict[str, Callable]):
        self.metrics = metrics
        self.results = pd.DataFrame()

    def run(self, 
        problems: List[OptimizationProblem],
        solvers: Dict[str, HybridSolver],
        iterations: int = 3):
        
        records = []
        for problem in problems:
            for name, solver in solvers.items():
                for _ in range(iterations):
                    start = time.perf_counter()
                    result = solver.solve(problem)
                    elapsed = time.perf_counter() - start
                    
                    record = {
                        'problem': type(problem).__name__,
                        'solver': name,
                        'runtime': elapsed,
                        'solution_quality': problem.evaluate_solution(result['solution']),
                        'converged': result.get('converged', False)
                    }
                    
                    for metric, fn in self.metrics.items():
                        record[metric] = fn(result)
                    
                    records.append(record)
        
        self.results = pd.DataFrame(records)
        return self

    def visualize(self):
        fig, axs = plt.subplots(1, 2, figsize=(14, 5))
        
        # Runtime plot
        self.results.groupby('solver')['runtime'].mean().plot.bar(ax=axs[0])
        axs[0].set_title('Average Runtime Comparison')
        axs[0].set_ylabel('Seconds')
        
        # Quality plot
        self.results.groupby('solver')['solution_quality'].mean().plot.bar(ax=axs[1])
        axs[1].set_title('Solution Quality Comparison')
        axs[1].set_ylabel('Objective Value')
        
        return fig