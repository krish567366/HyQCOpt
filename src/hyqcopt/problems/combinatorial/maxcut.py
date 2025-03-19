import numpy as np
from typing import Tuple, Any
from hyqcopt.core.interfaces import OptimizationProblem

class MaxCut(OptimizationProblem):
    def __init__(self, graph: np.ndarray):
        self.graph = graph
        self.n_nodes = graph.shape[0]

    def to_hamiltonian(self) -> Tuple[np.ndarray, float]:
        h = np.zeros(self.n_nodes)
        J = -0.5 * self.graph
        return J, h, 0.0

    def evaluate_solution(self, solution: np.ndarray) -> float:
        return 0.5 * np.sum(self.graph * (1 - np.outer(solution, solution)))

    @classmethod
    def validate_solution(cls, solution: np.ndarray) -> bool:
        return isinstance(solution, np.ndarray) and solution.ndim == 1

    @classmethod
    def random_instance(cls, n_nodes: int):
        graph = np.triu(np.random.rand(n_nodes, n_nodes))
        graph = graph + graph.T - 2 * np.diag(graph.diagonal())
        return cls(graph)