from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    username: str
    password: str
    role: Optional[str] = 'user'