# app/main.py
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
from app.settings import settings
from app.auth import router as auth_router
from app.rbac import require_role
from app.ai_client import send_message_to_ai

app = FastAPI(title="MCP SRE Assistant")
app.add_middleware(SessionMiddleware, secret_key=settings.session_secret_key)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.templates = Jinja2Templates(directory="app/templates")
app.include_router(auth_router)

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return app.templates.TemplateResponse("base.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, user=Depends(require_role("admin", "user", "viewer"))):
    return app.templates.TemplateResponse("dashboard.html", {"request": request, "user": user})

@app.get("/admin", response_class=HTMLResponse)
def admin_page(request: Request, user=Depends(require_role("admin"))):
    return app.templates.TemplateResponse("admin.html", {"request": request, "user": user})

@app.post("/chat", response_class=HTMLResponse)
async def chat(request: Request, message: str = Form(...), user=Depends(require_role("admin", "user"))):
    ai_resp = await send_message_to_ai(message)
    return app.templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "user": user, "last_message": message, "ai_response": ai_resp.get("reply")}
    )
