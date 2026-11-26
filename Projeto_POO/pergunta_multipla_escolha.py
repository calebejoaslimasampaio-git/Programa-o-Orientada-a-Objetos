from pergunta import Pergunta


class PerguntaMultiplaEscolha(Pergunta):

    def __init__(self, enunciado, alternativas, resposta_correta, pontos=10):
        super().__init__(enunciado, resposta_correta, pontos)

        self.alternativas = alternativas

    def verificar_resposta(self, resposta):
        return resposta.strip().lower() == self.resposta_correta.strip().lower()