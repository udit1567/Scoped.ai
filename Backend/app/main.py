from fastapi import FastAPI
from app.api import auth, projects, documents, chat
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title="Scope.ai")

app.include_router(auth.router, prefix="/auth")
app.include_router(projects.router, prefix="/projects")
app.include_router(documents.router, prefix="/documents")
app.include_router(chat.router, prefix="/chat")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/demo")
def demo_route():
    return {
        "status": "success",
        "message": "Demo API is working",
        "data": {
            "app": "Scoped.ai",
            "version": "1.0.0",
            "features": ["auth", "projects", "documents", "chat"]
        }
    }