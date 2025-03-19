from contextlib import contextmanager
from .factory import SolverFactory
from .config import RuntimeConfig

@contextmanager
def distributed_session(executor, strategy='parameter'):
    original_config = RuntimeConfig.get_config()
    RuntimeConfig.set_distributed(True, executor)
    RuntimeConfig.config.partition_strategy = strategy
    try:
        yield
    finally:
        RuntimeConfig.config = original_config

@contextmanager
def grover_session(iterations=3):
    original_config = RuntimeConfig.get_config()
    RuntimeConfig.enable_grover(True)
    try:
        yield
    finally:
        RuntimeConfig.config = original_config

def create_solver(solver_type, **kwargs):
    """Public API for solver creation"""
    return SolverFactory.get_solver(solver_type, **kwargs)