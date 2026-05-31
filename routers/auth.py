from fastapi import APIRouter, Header, Depends, HTTPException
from auth import crear_token, validar_token
from fastapi.security import OAuth2PasswordBearer
from models.login import Login

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

router = APIRouter()

@router.post("/login")
def login(datos: Login):
    if (datos.username != "admin" or datos.password != "1234"):
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas"
        )

    token = crear_token({"sub": datos.username})

    return {"access_token": token}

@router.get("/perfil")
def perfil(token: str = Depends(oauth2_scheme)):
    payload = validar_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

    return {"usuario": payload["sub"]}