import pytest
import numpy as np
from hyqcopt.algorithms.qaoa import QAOA
from hyqcopt.problems.combinatorial.maxcut import MaxCut

class MockBackend:
    def construct_ansatz(self, params):
        return "mock_circuit"
    
    def execute(self, circuit, shots):
        return {'101': 0.7, '010': 0.3}

@pytest.fixture
def maxcut_problem():
    graph = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    return MaxCut(graph)

def test_qaoa_solve(maxcut_problem):
    backend = MockBackend()
    qaoa = QAOA(backend, maxiter=5)
    result = qaoa.solve(maxcut_problem)
    
    assert 'solution' in result
    assert 'energy' in result
    assert isinstance(result['parameters'], np.ndarray)