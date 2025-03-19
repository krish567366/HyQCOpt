from typing import Protocol, runtime_checkable

@runtime_checkable
class HybridSolver(Protocol):
    def solve(self, problem, **kwargs) -> dict:
        ...
    
    def calibrate(self) -> None:
        ...
        
@runtime_checkable
class DistributedSolver(Protocol):
    def scale_workers(self, n_workers: int) -> None:
        ...
    
    def get_network_latency(self) -> float:
        ...