from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple, Protocol
import numpy as np

class QuantumBackend(Protocol):
    """Protocol defining quantum backend requirements"""
    @abstractmethod
    def execute(self, circuit: Any, shots: int) -> Dict[str, float]:
        ...
    
    @abstractmethod
    def construct_ansatz(self, params: np.ndarray) -> Any:
        ...

class OptimizationProblem(ABC):
    """Abstract base class for optimization problems"""
    @abstractmethod
    def to_hamiltonian(self) -> Tuple[np.ndarray, float]:
        """Convert problem to Ising Hamiltonian (matrix form)"""
        ...
    
    @abstractmethod
    def evaluate_solution(self, solution: Any) -> float:
        """Evaluate solution quality"""
        ...
    
    @classmethod
    @abstractmethod
    def validate_solution(cls, solution: Any) -> bool:
        """Validate solution feasibility"""
        ...

class HybridSolver(ABC):
    """Abstract base class for hybrid solvers"""
    @abstractmethod
    def solve(self, 
            problem: OptimizationProblem,
            backend: QuantumBackend,
            **kwargs) -> Dict[str, Any]:
        ...
    
    @classmethod
    def get_hyperparameters(cls) -> Dict[str, Any]:
        """Get solver hyperparameters"""
        return {}