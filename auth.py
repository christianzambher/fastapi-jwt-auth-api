from jose import jwt
from datetime import datetime, timedelta
from jose import JWTError
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

def crear_token(datos: dict):
    datos_copia = datos.copy()
    expiracion = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    datos_copia.update({"exp": expiracion})

    return jwt.encode(datos_copia, SECRET_KEY, algorithm=ALGORITHM)

def validar_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        return None