import numpy as np
from typing import Tuple
from hyqcopt.core.exceptions import ConversionError

def qubo_to_ising(Q: np.ndarray) -> Tuple[np.ndarray, float]:
    """Convert QUBO matrix to Ising model parameters"""
    try:
        J = 0.25 * Q
        h = -0.5 * np.diag(Q) - 0.5 * Q.sum(axis=0)
        offset = 0.5 * Q.sum() + 0.5 * np.diag(Q).sum()
        return J, h, offset
    except Exception as e:
        raise ConversionError(f"QUBO to Ising conversion failed: {str(e)}")