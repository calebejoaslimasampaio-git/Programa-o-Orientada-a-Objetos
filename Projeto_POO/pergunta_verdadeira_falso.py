from pergunta import Pergunta


class PerguntaVerdadeiroFalso(Pergunta):

    def verificar_resposta(self, resposta):
        return resposta.strip().lower() == self.resposta_correta.strip().lower()