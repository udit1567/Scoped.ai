from fastapi import APIRouter, Depends
from app.core.security import get_current_user

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/")
def get_projects(current_user: str = Depends(get_current_user)):
    return {
        "message": "Projects data",
        "user": current_user
    }
