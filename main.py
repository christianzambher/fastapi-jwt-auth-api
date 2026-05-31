from fastapi import FastAPI

from routers.auth import auth_router
from routers.usuarios import router as usuarios_router

from database import crear_tabla, crear_usuario

app = FastAPI()

crear_tabla()

app.include_router(auth_router)
app.include_router(usuarios_router)