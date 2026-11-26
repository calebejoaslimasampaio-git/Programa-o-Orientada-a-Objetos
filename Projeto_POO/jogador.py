class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.__pontuacao = 0
        self.acertos = 0

    def registrar_acerto(self, pontos):
        self.__pontuacao += pontos
        self.acertos += 1

    def consultar_pontuacao(self):
        return self.__pontuacao

    def zerar_pontuacao(self):
        self.__pontuacao = 0
        self.acertos = 0