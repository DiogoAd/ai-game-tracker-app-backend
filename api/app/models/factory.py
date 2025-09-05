from app.models.fifa import FifaModel
from app.models.lol import LolModel
from app.models.base import GameModel

class ModelFactory:
    @staticmethod
    def get_model(game_type: str) -> GameModel:
        game_type = game_type.upper()
        if game_type == "FIFA":
            return FifaModel()
        elif game_type == "LOL":
            return LolModel()
        else:
            raise ValueError(f"Unknown game type: {game_type}")
