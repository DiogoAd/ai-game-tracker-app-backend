import mysql.connector
from app.config import settings

def get_db_connection():
    return mysql.connector.connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME
    )

def create_game_log(game_type: str) -> (int, str):
    """Cria um log na tabela games com nome incremental"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM games WHERE name LIKE %s", (f"{game_type}%",))
    count = cursor.fetchone()[0] + 1
    game_name = f"{game_type} {count}"
    cursor.execute("INSERT INTO games (name) VALUES (%s)", (game_name,))
    conn.commit()
    game_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return game_id, game_name
