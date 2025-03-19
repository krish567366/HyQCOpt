from typing import Callable, Dict, Any
import numpy as np
from scipy.optimize import OptimizeResult, minimize

class ClassicalOptimizer:
    def __init__(self, 
            method: str = 'L-BFGS-B',
            jac: Callable = None,
            hess: Callable = None):
        self.method = method
        self.jac = jac
        self.hess = hess

    def optimize(self,
            objective: Callable,
            initial_params: np.ndarray,
            bounds: Any = None) -> OptimizeResult:
        return minimize(objective,
                    initial_params,
                    method=self.method,
                    jac=self.jac,
                    hess=self.hess,
                    bounds=bounds)