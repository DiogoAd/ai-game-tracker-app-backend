from pydantic import BaseModel

# Receber qualquer jogo
class GameReceive(BaseModel):
    game_type: str  # "FIFA" ou "LoL"
    data: dict      # No futuro vai ser imagem bitmap

# Retorno do endpoint
class GameResponse(BaseModel):
    game_id: int
    game_name: str
    extracted_data: dict
