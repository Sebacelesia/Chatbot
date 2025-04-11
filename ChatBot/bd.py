import sqlite3
from datetime import datetime

DB_PATH = "bot_data.db"

def crear_tablas():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                user_id INTEGER PRIMARY KEY,
                nombre TEXT,
                username TEXT,
                creado_en TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS conversaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                mensaje TEXT NOT NULL,
                respuesta TEXT,
                timestamp TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES usuarios(user_id)
            )
        """)
        conn.commit()

def registrar_usuario(user_id: int, nombre: str = None, username: str = None):
    creado_en = datetime.now().isoformat(sep=' ', timespec='seconds')
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO usuarios (user_id, nombre, username, creado_en)
            VALUES (?, ?, ?, ?)
        """, (user_id, nombre, username, creado_en))
        conn.commit()

def registrar_conversacion(user_id: int, mensaje: str, respuesta: str):
    timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO conversaciones (user_id, mensaje, respuesta, timestamp)
            VALUES (?, ?, ?, ?)
        """, (user_id, mensaje, respuesta, timestamp))
        conn.commit()

def obtener_historial(user_id: int, limite: int = 5):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT mensaje, respuesta, timestamp
            FROM conversaciones
            WHERE user_id = ?
            ORDER BY timestamp DESC
            LIMIT ?
        """, (user_id, limite))
        return cursor.fetchall()
