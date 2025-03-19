from __future__ import annotations
from typing import Dict, Any, Tuple
import numpy as np
from scipy.optimize import minimize
from hyqcopt.core.interfaces import OptimizationProblem, HybridSolver, QuantumBackend
from hyqcopt.classical.optimizers import ClassicalOptimizer
from hyqcopt.algorithms.grover import GroverOptimizer

class QAOA(HybridSolver):
    def __init__(self, 
            backend: QuantumBackend,
            optimizer: str = 'COBYLA',
            maxiter: int = 100,
            shots: int = 1024):
        self.backend = backend
        self.optimizer = optimizer
        self.maxiter = maxiter
        self.shots = shots

    def solve(self, 
            problem: OptimizationProblem,
            initial_params: np.ndarray = None,
            **kwargs) -> Dict[str, Any]:
        
        # Initialize parameters
        p = kwargs.get('p', 1)  # QAOA layers
        if initial_params is None:
            initial_params = np.random.uniform(0, 2*np.pi, size=2*p)
            
        # Store problem reference
        self.problem = problem
        
        # Optimization loop
        result = minimize(self._expectation,
                        initial_params,
                        method=self.optimizer,
                        options={'maxiter': self.maxiter})
        
        # Final solution
        best_solution = self._get_best_solution(result.x)
        
        return {
            'parameters': result.x,
            'solution': best_solution,
            'energy': result.fun,
            'history': result.get('history', []),
            'metadata': {
                'optimizer': self.optimizer,
                'layers': p,
                'shots': self.shots
            }
        }

    def _expectation(self, params: np.ndarray) -> float:
        circuit = self.backend.construct_ansatz(params)
        counts = self.backend.execute(circuit, self.shots)
        return sum(prob * self.problem.evaluate_solution(self._parse_counts(key)) 
                for key, prob in counts.items())

    def _parse_counts(self, bitstring: str) -> np.ndarray:
        return np.array([int(b) for b in bitstring])

    def _get_best_solution(self, params: np.ndarray) -> np.ndarray:
        circuit = self.backend.construct_ansatz(params)
        counts = self.backend.execute(circuit, shots=1)
        return self._parse_counts(max(counts, key=counts.get))