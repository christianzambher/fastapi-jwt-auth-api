from fastapi import APIRouter, Header, Depends, HTTPException
from auth import crear_token, validar_token
from fastapi.security import OAuth2PasswordBearer
from models.login import Login
from database import obtener_usuario_username
from security import verify_password

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

auth_router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)

def obtener_usuario_actual(
    token: str = Depends(oauth2_scheme)
):
    payload = validar_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

    return payload

@auth_router.post("/login")
def login(datos: Login):
    usuario = obtener_usuario_username(datos.username)

    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="Credenciales incorrectas"
        )

    if not verify_password(datos.password, usuario[2]):
        raise HTTPException(
            status_code=401,
            detail="Credenciales incorrectas"
        )

    token = crear_token({"sub": usuario[1], "role": usuario[3]})

    return {"access_token": token}

@auth_router.get("/perfil")
def perfil(token: str = Depends(oauth2_scheme)):
    payload = validar_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

    return {"usuario": payload["sub"], "role": payload["role"]}

def verificar_admin(
    usuario=Depends(obtener_usuario_actual)
):
    if usuario["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Acceso denegado"
        )

    return usuario