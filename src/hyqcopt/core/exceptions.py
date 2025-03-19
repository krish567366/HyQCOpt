# src/hyqcopt/core/exceptions.py

from typing import Any 

class HyQCOptError(Exception):
    """Base exception class for all framework errors"""
    error_code: int = 0000
    component: str = "core"
    
    def __init__(self, message: str, context: dict | None = None):
        super().__init__(message)
        self.context = context or {}
        
    def __str__(self) -> str:
        return f"[{self.error_code}] {super().__str__()} | Component: {self.component}"

class ConversionError(HyQCOptError):
    """Raised during quantum-classical conversions"""
    error_code = 1001
    component = "converters"
    
    def __init__(self, conversion_type: str, original_error: Exception | None = None):
        message = f"{conversion_type} conversion failed"
        context = {
            "original_error": str(original_error) if original_error else None,
            "conversion_type": conversion_type
        }
        super().__init__(message, context)

class BackendError(HyQCOptError):
    """Base error for quantum backend issues"""
    error_code = 2000
    component = "backends"

class BackendConnectionError(BackendError):
    """Failed to connect to quantum backend"""
    error_code = 2001
    
    def __init__(self, backend_name: str, reason: str):
        message = f"Connection to {backend_name} failed: {reason}"
        super().__init__(message, {"backend": backend_name})

class BackendExecutionError(BackendError):
    """Quantum circuit execution failed"""
    error_code = 2002
    
    def __init__(self, circuit_info: dict, shots: int):
        message = f"Failed to execute {circuit_info.get('n_qubits', 'unknown')}-qubit circuit ({shots} shots)"
        super().__init__(message, {"circuit": circuit_info, "shots": shots})

class ProblemFormulationError(HyQCOptError):
    """Base error for problem formulation issues"""
    error_code = 3000
    component = "problems"

class InvalidHamiltonianError(ProblemFormulationError):
    """Invalid Hamiltonian construction"""
    error_code = 3001
    
    def __init__(self, matrix_shape: tuple, reason: str):
        message = f"Invalid Hamiltonian matrix {matrix_shape}: {reason}"
        super().__init__(message, {"shape": matrix_shape})

class SolverError(HyQCOptError):
    """Base error for optimization solvers"""
    error_code = 4000
    component = "solvers"

class SolverConfigurationError(SolverError):
    """Invalid solver configuration"""
    error_code = 4001
    
    def __init__(self, parameter: str, value: Any, valid_range: str):
        message = f"Invalid {parameter}={value}. Valid range: {valid_range}"
        super().__init__(message, {
            "parameter": parameter,
            "value": value,
            "valid_range": valid_range
        })

class DistributedComputingError(HyQCOptError):
    """Base error for distributed computing"""
    error_code = 5000
    component = "distributed"

class WorkerAllocationError(DistributedComputingError):
    """Failed to allocate distributed workers"""
    error_code = 5001
    
    def __init__(self, requested: int, available: int):
        message = f"Requested {requested} workers, only {available} available"
        super().__init__(message, {
            "requested_workers": requested,
            "available_workers": available
        })