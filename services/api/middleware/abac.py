# services/middleware/abac.py
def check_access(user: User, resource: Resource):
    if user.role == 'admin':
        return True
    if resource.type == 'job' and user.id != resource.owner_id:
        raise HTTPException(403, "Access denied")
    if resource.sensitivity == 'high' and not user.mfa_enabled:
        raise HTTPException(403, "MFA required")
    return Trues