# FastAPI JWT Auth API

Proyecto educativo desarrollado con FastAPI para comprender autenticación basada en JWT.

## Características

- JWT Authentication
- OAuth2 Password Flow
- Role-Based Access Control (RBAC)
- Password Hashing con bcrypt
- SQLite Database
- CRUD de Usuarios
- Variables de Entorno (.env)
- Swagger UI Integrado
- Arquitectura Modular

---

## Tecnologías Utilizadas

- Python 3.13
- FastAPI
- SQLite
- Python-JOSE
- Passlib
- Bcrypt
- Uvicorn
- Pydantic

---

## Estructura del Proyecto

```text
fastapi-jwt-auth-api/
│
├── database/
│   └── usuarios.db
│
├── models/
│   └── usuario.py
│
├── routers/
│   ├── auth.py
│   └── usuarios.py
│
├── auth.py
├── config.py
├── database.py
├── security.py
├── main.py
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## Instalación

### Clonar repositorio

```bash
git clone https://github.com/TU_USUARIO/fastapi-jwt-auth-api.git

cd fastapi-jwt-auth-api
```

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar entorno virtual

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Variables de Entorno

Crear archivo:

```text
.env
```

Basado en:

```env
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Ejecutar Proyecto

```bash
python -m uvicorn main:app --reload
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## Flujo de Autenticación

### Registrar Usuario

```http
POST /usuarios
```

Ejemplo:

```json
{
  "username": "admin",
  "password": "123456",
  "role": "admin"
}
```

---

### Login

```http
POST /auth/login
```

OAuth2 Password Flow.

Swagger genera automáticamente el token JWT.

---

### Perfil

```http
GET /auth/perfil
```

Requiere token JWT válido.

---

## Roles

Actualmente existen dos roles:

### user

Puede:

- Consultar información permitida
- Autenticarse

### admin

Puede:

- Eliminar usuarios
- Acceder a recursos protegidos para administradores

---

## Ejemplo de Payload JWT

```json
{
  "sub": "admin",
  "role": "admin",
  "exp": 9999999999
}
```

---

## Seguridad Implementada

### Hashing de Contraseñas

Las contraseñas no se almacenan en texto plano.

Se utiliza:

- SHA-256
- bcrypt

para proteger credenciales de usuario.

### JWT

Los tokens incluyen:

- Usuario autenticado
- Rol asignado
- Fecha de expiración

---

## Endpoints

| Método | Endpoint | Descripción |
|----------|----------|----------|
| POST | /usuarios | Registrar usuario |
| GET | /usuarios | Listar usuarios |
| GET | /usuarios/{id} | Obtener usuario |
| PUT | /usuarios/{id} | Actualizar usuario |
| DELETE | /usuarios/{id} | Eliminar usuario (admin) |
| POST | /auth/login | Generar token |
| GET | /auth/perfil | Perfil autenticado |

---

## Aprendizajes del Proyecto

- Arquitectura modular con FastAPI
- JWT Authentication
- OAuth2 Integration
- RBAC
- SQLite Persistence
- Password Hashing
- Variables de Entorno
- Manejo de Dependencias
- Documentación automática con OpenAPI

---

## Autor

Christian Zambrano