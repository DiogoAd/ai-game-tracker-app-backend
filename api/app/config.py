import os

class Settings:
    DB_HOST = os.getenv("DB_HOST", "db")  # fallback para "db"
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_USER = os.getenv("DB_USER", "appuser")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "apppass")
    DB_NAME = os.getenv("DB_NAME", "gamesdb")


settings = Settings()
