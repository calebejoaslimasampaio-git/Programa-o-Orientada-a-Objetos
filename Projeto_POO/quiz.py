class Quiz:

    def __init__(self, perguntas, jogador):
        self.perguntas = perguntas
        self.jogador = jogador
        self.indice_atual = 0

    def obter_pergunta_atual(self):
        return self.perguntas[self.indice_atual]

    def responder(self, resposta):
        pergunta = self.obter_pergunta_atual()

        if pergunta.verificar_resposta(resposta):
            self.jogador.registrar_acerto(pergunta.pontos)
            return True

        return False

    def proxima_pergunta(self):
        if self.indice_atual < len(self.perguntas) - 1:
            self.indice_atual += 1
            return True

        return False

    def quantidade_perguntas(self):
        return len(self.perguntas)