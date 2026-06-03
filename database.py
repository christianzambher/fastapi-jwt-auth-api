import sqlite3
import os
from fastapi import HTTPException
from security import hash_password 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, 'database')
DB_PATH = os.path.join(DB_DIR, 'usuarios.db')

def conectar():
    os.makedirs(DB_DIR, exist_ok=True)
    return sqlite3.connect(DB_PATH)

def crear_tabla():
    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'user'
    )
    """)

    conexion.commit()
    conexion.close()

def crear_usuario(username, password, role='user'):
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
        INSERT INTO usuarios (username, password, role)
        VALUES (?, ?, ?)
        """, (username, hash_password(password), role))

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
    SELECT id, username, role
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

def obtener_usuario_id(id):
    conexion = None
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        SELECT id, username
        FROM usuarios
        WHERE id = ? 
        """, (id, ))

        if not cursor.fetchone():
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )

        usuario = cursor.fetchone()
        conexion.close()
    except sqlite3.IntegrityError:
        raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )
    return usuario


def actualizar_usuario(id, username):
    conexion = None
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        UPDATE usuarios
        SET username = ?
        WHERE id = ? 
        """, (username, id))

        conexion.commit()

        filas = cursor.rowcount

        return filas
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )
    finally:
        if conexion:
            conexion.close()

def eliminar_usuario(id):
    conexion = None
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        DELETE FROM usuarios
        WHERE id = ? 
        """, (id, ))

        conexion.commit()

        filas = cursor.rowcount

        return filas
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )
    finally:
        if conexion:
            conexion.close()