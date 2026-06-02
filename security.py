import hashlib
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

def hash_password(password: str):
    password_bytes = hashlib.sha256(password.encode('utf-8')).hexdigest().encode('utf-8')
    return pwd_context.hash(password_bytes)

def verify_password(plain_password: str, hashed_password: str):
    plain_password_bytes = hashlib.sha256(plain_password.encode('utf-8')).hexdigest().encode('utf-8')
    return pwd_context.verify(plain_password_bytes, hashed_password)