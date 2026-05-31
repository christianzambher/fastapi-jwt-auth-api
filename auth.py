from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "mi_clave_super_secreta"
ALGORITHM = "HS256"

def crear_token(datos: dict):
    datos_copia = datos.copy()
    expiracion = datetime.utcnow() + timedelta(minutes=30)

    datos_copia.update({"exp": expiracion})

    return jwt.encode(datos_copia, SECRET_KEY, algorithm=ALGORITHM)