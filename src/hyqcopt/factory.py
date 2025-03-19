# src/hyqcopt/factory.py
from typing import Any
from .algorithms import QAOA, GroverOptimizer, DistributedHybridSolver
from .config import RuntimeConfig

class GroverEnhancer:
    """Decorator to add Grover amplification to any solver"""
    def __init__(self, base_solver: Any):
        self.base_solver = base_solver
        
    def solve(self, problem: Any, **kwargs) -> dict:
        # Pre-processing with Grover
        grover_result = self._grover_amplification(problem)
        
        # Pass enhanced solution to base solver
        return self.base_solver.solve(
            problem,
            initial_params=grover_result['params'],
            **kwargs
        )
    
    def _grover_amplification(self, problem):
        # Implementation from earlier GroverOptimizer
        pass

class SolverFactory:
    @staticmethod
    def get_solver(solver_type: str = 'QAOA', **kwargs):
        config = RuntimeConfig.get_config()
        
        # Base solver creation
        if solver_type == 'QAOA':
            solver = QAOA(**kwargs)
        elif solver_type == 'Grover':
            solver = GroverOptimizer(**kwargs)
        else:
            raise ValueError(f"Unknown solver type: {solver_type}")
        
        # Add distributed layer
        if config.distributed:
            solver = DistributedHybridSolver(
                base_solver=solver,
                executor=config.executor,
                partition_strategy=config.partition_strategy
            )
        
        # Add Grover enhancement
        if config.grover_enhance:
            solver = GroverEnhancer(solver)
            
        return solver