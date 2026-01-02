from fastapi import APIRouter

router = APIRouter()

@router.post("/create")
def create_project():
    return {"message": "Project created"}

@router.get("/")
def list_projects():
    return {"projects": []}
