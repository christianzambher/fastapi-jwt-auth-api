# FastAPI JWT Auth API

Proyecto educativo desarrollado con FastAPI para comprender autenticación basada en JWT.

## Tecnologías

- Python
- FastAPI
- Uvicorn
- Python-JOSE
- JWT
- OAuth2

## Funcionalidades

- Generación de JWT
- Endpoint de login
- Expiración de tokens
- Protección de rutas
- Obtencion de usaurio autenticado
- Registro de usuarios
- Login con JWT
- Rutas protegidas
- Hash de contraseñas con bcrypt
- CRUD completo de usuarios

## Endpoints

### Login

POST /login

Genera un token JWT para el usuario autenticado.

### Perfil

GET /perfil

Ruta protegida que requiere un JWT válido.

## Flujo de autenticación

1. El usuario realiza login.
2. La API genera un JWT.
3. El cliente almacena el token.
4. El token es enviado en el header Authorization.
5. La API valida el JWT.
6. Se permite el acceso a rutas protegidas.

## Ejecutar

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```