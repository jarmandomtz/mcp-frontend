# app/rbac.py
from fastapi import Depends, HTTPException, Request

def require_role(*allowed_roles: str):
    def dependency(request: Request):
        user = request.session.get("user")
        if not user:
            raise HTTPException(status_code=401, detail="Not authenticated")
        if user["role"] not in allowed_roles:
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return dependency
