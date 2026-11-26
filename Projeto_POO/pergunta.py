from abc import ABC, abstractmethod


class Pergunta(ABC):

    def __init__(self, enunciado, resposta_correta, pontos=10):
        self.enunciado = enunciado
        self.resposta_correta = resposta_correta
        self.pontos = pontos

    @abstractmethod
    def verificar_resposta(self, resposta):
        pass