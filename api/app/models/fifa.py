from .base import GameModel
from app.db import get_db_connection

class FifaModel(GameModel):
    def extract(self, data: dict) -> dict:
        return {
            "possession_percent": data["possession_percent"],
            "goals_scored": data["goals_scored"],
            "goals_conceded": data["goals_conceded"]
        }

    def load(self, game_id: int, extracted_data: dict):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO fifa (game_id, possession_percent, goals_scored, goals_conceded)
            VALUES (%s, %s, %s, %s)
        """, (
            game_id,
            extracted_data["possession_percent"],
            extracted_data["goals_scored"],
            extracted_data["goals_conceded"]
        ))
        conn.commit()
        cursor.close()
        conn.close()
