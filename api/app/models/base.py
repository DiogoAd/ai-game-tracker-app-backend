from abc import ABC, abstractmethod

class GameModel(ABC):
    @abstractmethod
    def extract(self, data: dict) -> dict:
        """Extrai dados do JSON recebido"""
        pass

    @abstractmethod
    def load(self, game_id: int, extracted_data: dict):
        """Guarda os dados extraídos na tabela correspondente"""
        pass
