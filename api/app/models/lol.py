from .base import GameModel
from app.db import get_db_connection

class LolModel(GameModel):
    def extract(self, data: dict) -> dict:
        return {
            "kills": data["kills"],
            "deaths": data["deaths"],
            "assists": data["assists"]
        }

    def load(self, game_id: int, extracted_data: dict):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO lol (game_id, kills, deaths, assists)
            VALUES (%s, %s, %s, %s)
        """, (
            game_id,
            extracted_data["kills"],
            extracted_data["deaths"],
            extracted_data["assists"]
        ))
        conn.commit()
        cursor.close()
        conn.close()
