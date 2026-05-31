import sqlite3
from fastapi import HTTPException

def conectar():
    return sqlite3.connect('database/usuarios.db')

def crear_tabla():
    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conexion.commit()
    conexion.close()

def crear_usuario(username, password):
    conexion = None
    try:
        usuario = obtener_usuario_username(username)
        if usuario:
            raise HTTPException(
                status_code=400,
                detail="El nombre de usuario ya existe"
            )

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        INSERT INTO usuarios (username, password)
        VALUES (?,?)
        """, (username, password))

        conexion.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="El nombre de usuario ya existe"
        )
    finally:
        if conexion:
            conexion.close()

def obtener_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT id, username 
    FROM usuarios
     """)

    usuarios = cursor.fetchall()

    conexion.close()

    return usuarios

def obtener_usuario_username(username):
    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
    SELECT * 
    FROM usuarios
    WHERE username = ? 
    """, (username, ))

    usuario = cursor.fetchone()

    conexion.close()

    return usuario