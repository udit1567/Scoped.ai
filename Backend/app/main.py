from fastapi import FastAPI
from app.api import auth, projects, documents, chat

app = FastAPI(title="Scope.ai")

app.include_router(auth.router, prefix="/auth")
app.include_router(projects.router, prefix="/projects")
app.include_router(documents.router, prefix="/documents")
app.include_router(chat.router, prefix="/chat")
