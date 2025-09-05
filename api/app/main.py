from fastapi import FastAPI
from app.schemas import GameReceive, GameResponse
from app.db import create_game_log
from app.models.factory import ModelFactory

app = FastAPI(title="Game Recognizer MVP", version="1.0.0")

@app.post("/games/receive", response_model=GameResponse)
def receive_game(game: GameReceive):
    # 1️⃣ Criar log do jogo
    print("Recebido jogo:", game)
    game_id, game_name = create_game_log(game.game_type)

    # 2️⃣ Obter model via Factory
    model = ModelFactory.get_model(game.game_type)
    print("Usando modelo:", model)

    # 3️⃣ Extrair dados
    extracted_data = model.extract(game.data)
    print("Dados extraídos:", extracted_data)

    # 4️⃣ Guardar dados na tabela correta
    model.load(game_id, extracted_data)

    # 5️⃣ Retornar resposta
    return GameResponse(
        game_id=game_id,
        game_name=game_name,
        extracted_data=extracted_data
    )
