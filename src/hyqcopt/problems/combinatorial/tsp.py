import numpy as np
from typing import Tuple
from hyqcopt.core.interfaces import OptimizationProblem

class TSP(OptimizationProblem):
    def __init__(self, distance_matrix: np.ndarray):
        self.n = distance_matrix.shape[0]
        self.distance_matrix = distance_matrix
        self._validate_matrix()

    def _validate_matrix(self):
        if self.distance_matrix.shape != (self.n, self.n):
            raise ValueError("Invalid distance matrix dimensions")
        if not np.allclose(self.distance_matrix, self.distance_matrix.T):
            raise ValueError("Distance matrix must be symmetric")

    def to_hamiltonian(self) -> Tuple[np.ndarray, float]:
        """Convert TSP to Ising Hamiltonian using penalty method"""
        # Implementation of transformation logic
        H = np.zeros((self.n**2, self.n**2))
        penalty = 1.5 * np.max(self.distance_matrix)
        
        # Constraint terms
        for i in range(self.n):
            for t in range(self.n):
                H[i*self.n + t, i*self.n + t] += -penalty
                for t_prime in range(t+1, self.n):
                    H[i*self.n + t, i*self.n + t_prime] += penalty/2
                    H[i*self.n + t_prime, i*self.n + t] += penalty/2

        # Objective terms
        for t in range(self.n):
            i, j = t, (t+1) % self.n
            for u in range(self.n):
                for v in range(self.n):
                    H[u*self.n + i, v*self.n + j] += self.distance_matrix[u,v]/4
                    
        return H, 0.0

    def evaluate_solution(self, solution: np.ndarray) -> float:
        """Calculate total tour length"""
        return sum(self.distance_matrix[solution[i], solution[i+1]] 
                for i in range(len(solution)-1))