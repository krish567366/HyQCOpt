from qiskit import QuantumCircuit, Aer, transpile
from hyqcopt.core.interfaces import QuantumBackend
import numpy as np
from typing import Any, Dict, Protocol

class QiskitQAOABackend(QuantumBackend):
    def __init__(self, simulator: str = 'aer_simulator'):
        self.simulator = Aer.get_backend(simulator)
        self.shots = 1024

    def construct_ansatz(self, params: np.ndarray) -> QuantumCircuit:
        """Construct QAOA circuit with given parameters"""
        p = len(params) // 2  # Number of QAOA layers
        beta, gamma = params[:p], params[p:]
        
        qc = QuantumCircuit(self.n_qubits)
        # Initial state
        qc.h(range(self.n_qubits))
        
        # QAOA layers
        for layer in range(p):
            # Problem unitary
            for (i, j), weight in self.problem_edges.items():
                qc.rzz(2 * gamma[layer] * weight, i, j)
            # Mixer unitary
            qc.rx(2 * beta[layer], range(self.n_qubits))
            
        return qc

    def execute(self, circuit: QuantumCircuit, shots: int = 1024) -> Dict[str, float]:
        compiled = transpile(circuit, self.simulator)
        job = self.simulator.run(compiled, shots=shots)
        counts = job.result().get_counts()
        return {k: v/shots for k, v in counts.items()}