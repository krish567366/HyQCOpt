from fastapi import FastAPI, Depends
from hyqcopt import QAOA, VQE, TSPProblem
from .middleware.auth import validate_tenant

app = FastAPI()

@app.post("/jobs/{solver_type}")
async def submit_job(
    solver_type: str, 
    problem_data: dict,
    tenant: dict = Depends(validate_tenant)
):
    """Handle quantum job submissions"""
    
    solver = {
        "qaoa": QAOA(),
        "vqe": VQE()
    }[solver_type]
    
    problem = TSPProblem(problem_data['cities'])
    
    return {
        "job_id": str(uuid.uuid4()),
        "estimated_cost": solver.estimate_cost(problem),
        "tenant": tenant['id']
    }