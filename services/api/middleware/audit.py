# services/api/middleware/audit.py
async def audit_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    
    AuditLog.create(
        user=request.state.user.id,
        endpoint=request.url.path,
        duration=time.time() - start_time,
        status=response.status_code
    )
    
    return response