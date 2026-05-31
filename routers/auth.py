from fastapi import APIRouter
from auth import crear_token

router = APIRouter()

@router.post("/login")
def login():
    token = crear_token({"sub": "usuario"})

    return {"access_token": token}