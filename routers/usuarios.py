from fastapi import FastAPI, APIRouter, Depends, HTTPException
from routers.auth import verificar_admin, obtener_usuario_actual
from models.usuario import Usuario
from database import (
    crear_usuario, 
    obtener_usuarios, 
    obtener_usuario_id, 
    actualizar_usuario as actualizar_usuario_db, 
    eliminar_usuario as eliminar_usuario_db)

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

@router.post("/")
def registrar_usuario(usuario: Usuario):
    crear_usuario(usuario.username, usuario.password, usuario.role)
    return {"mensaje": "Usuario registrado exitosamente"}

@router.get("/")
def listar_usuarios():
    usuarios = obtener_usuarios()

    resultado = []

    for usuario in usuarios:
        resultado.append({
            "id": usuario[0],
            "username": usuario[1],
            "role": usuario[2]
        })

    return resultado

@router.get("/{id}")
def obtener_usuario(id: int):
    usuario = obtener_usuario_id(id)

    if not usuario:
        return usuario
    return {
        "id": usuario[0],
        "username": usuario[1],
        "role": usuario[2]
    }

@router.put("/usuarios/{id}")
def actualizar_usuario(id: int, usuario: Usuario):
    filas = actualizar_usuario_db(id, usuario.username)

    if filas == 0:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return {
        "mensaje": "Usuario actualizado"
    }

@router.delete("/usuarios/{id}")
def eliminar_usuario(id: int, admin=Depends(verificar_admin)):
    filas = eliminar_usuario_db(id)

    if filas == 0:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return {
        "mensaje": "Usuario eliminado"
    }