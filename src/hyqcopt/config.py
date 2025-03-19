from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class SolverConfig:
    distributed: bool = False
    executor: Optional[Any] = None
    partition_strategy: str = 'parameter'
    grover_enhance: bool = False

class RuntimeConfig:
    _instance = None
    config = SolverConfig()
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @classmethod
    def set_distributed(cls, enabled: bool, executor=None):
        cls.config.distributed = enabled
        if executor:
            cls.config.executor = executor
            
    @classmethod
    def enable_grover(cls, enabled: bool):
        cls.config.grover_enhance = enabled

    @classmethod
    def get_config(cls):
        return cls.config