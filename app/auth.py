# app/auth.py
from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from passlib.hash import argon2
from app.bigquery_client import fetch_user

router = APIRouter()

@router.get("/login")
def login_page(request: Request):
    #return request.app.templates.TemplateResponse("login.html", {"request": request})
    return request.app.templates.TemplateResponse(request,"login.html")

@router.post("/login")
def login(email: str = Form(...), password: str = Form(...), request: Request = None):
    row = fetch_user(email)
    if not row or not argon2.verify(password, row["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    request.session["user"] = {"email": row["email"], "role": row["role"]}
    return RedirectResponse(url="/dashboard", status_code=303)

@router.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=303)
