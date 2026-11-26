from pergunta_multipla_escolha import PerguntaMultiplaEscolha
from pergunta_verdadeira_falso import PerguntaVerdadeiroFalso


def criar_perguntas():

    perguntas = [

        PerguntaMultiplaEscolha(
            "Qual é a capital do Brasil?",
            ["São Paulo", "Brasília", "Rio de Janeiro", "Salvador"],
            "Brasília"
        ),

        PerguntaVerdadeiroFalso(
            "Python é uma linguagem de programação.",
            "Verdadeiro"
        ),

        PerguntaMultiplaEscolha(
            "Quanto é 5 x 5?",
            ["10", "15", "20", "25"],
            "25"
        ),

        PerguntaVerdadeiroFalso(
            "O Sol é um planeta.",
            "Falso"
        )

    ]

    return perguntas