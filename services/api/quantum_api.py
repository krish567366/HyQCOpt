from fastapi import FastAPI, Depends, HTTPException
from hyqcopt import QAOA, VQE, TSPProblem, get_job_metrics
from .auth import validate_tenant
from .models import JobRequest, TenantConfig

app = FastAPI()

@app.post("/jobs/submit")
async def submit_job(
    request: JobRequest,
    tenant: TenantConfig = Depends(validate_tenant)
):
    """Submit quantum job with tenant isolation"""
    
    # Enforce tenant limits
    if request.qubits > tenant.max_qubits:
        raise HTTPException(403, "Qubit limit exceeded")
    
    # Initialize solver from core package
    solver = QAOA() if request.solver_type == "qaoa" else VQE()
    
    # Execute via core package
    problem = TSPProblem(request.cities)
    result = solver.solve(problem)
    
    return {
        "job_id": str(uuid.uuid4()),
        "tenant": tenant.id,
        "estimated_cost": solver.estimate_cost(problem)
    }