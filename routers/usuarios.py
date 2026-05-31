from fastapi import FastAPI, APIRouter
from models.usuario import Usuario
from database import crear_usuario, obtener_usuarios

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

@router.post("/")
def registrar_usuario(usuario: Usuario):
    crear_usuario(usuario.username, usuario.password)
    return {"mensaje": "Usuario registrado exitosamente"}

@router.get("/")
def listar_usuarios():
    usuarios = obtener_usuarios()

    resultado = []

    for usuario in usuarios:
        resultado.append({
            "id": usuario[0],
            "username": usuario[1]
        })

    return resultado
