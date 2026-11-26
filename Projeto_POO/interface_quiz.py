import tkinter as tk

from jogador import Jogador
from quiz import Quiz
from perguntas import criar_perguntas
from pergunta_multipla_escolha import PerguntaMultiplaEscolha


class InterfaceQuiz:

    def __init__(self, janela):
        self.janela = janela

        self.janela.title("Hardcore Quiz")
        self.janela.geometry("600x450")
        janela.configure(bg="darkgray")

        self.quiz = None
        self.botoes_resposta = []

        self.mostrar_tela_inicial()

    def limpar_tela(self):
        for elemento in self.janela.winfo_children():
            elemento.destroy()

    def mostrar_tela_inicial(self):
        self.limpar_tela()

        titulo = tk.Label(
            self.janela,
            text="Hardcore Quiz",
            font=("Arial", 24, "bold")
            bg=("darkgray")
            
        )
        titulo.pack(pady=30)

        texto = tk.Label(
            self.janela,
            text="Digite seu nome para começar:",
            bg="darkgray"
        )
        texto.pack()

        self.campo_nome = tk.Entry(self.janela)
        self.campo_nome.pack(pady=10)

        botao = tk.Button(
            self.janela,
            text="Começar",
            command=self.iniciar_quiz
        )
        botao.pack(pady=20)

    def iniciar_quiz(self):
        nome = self.campo_nome.get().strip()

        if nome == "":
            nome = "Jogador"

        jogador = Jogador(nome)

        self.quiz = Quiz(criar_perguntas(), jogador)

        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        self.limpar_tela()
        self.botoes_resposta = []

        pergunta = self.quiz.obter_pergunta_atual()

        numero = self.quiz.indice_atual + 1
        total = self.quiz.quantidade_perguntas()

        progresso = tk.Label(
            self.janela,
            text=f"Pergunta {numero} de {total}"
            bg="darkgray"
        )
        progresso.pack(pady=15)

        enunciado = tk.Label(
            self.janela,
            text=pergunta.enunciado,
            font=("Arial", 16, "bold"),
            wraplength=500
            bg="darkgray"
        )
        enunciado.pack(pady=20)

        if isinstance(pergunta, PerguntaMultiplaEscolha):
            alternativas = pergunta.alternativas
        else:
            alternativas = ["Verdadeiro", "Falso"]

        for alternativa in alternativas:

            botao = tk.Button(
                self.janela,
                text=alternativa,
                width=30,
                command=lambda resposta=alternativa: self.responder(resposta)
            )

            botao.pack(pady=5)
            self.botoes_resposta.append(botao)

    def responder(self, resposta):
        resultado = self.quiz.responder(resposta)

        for botao in self.botoes_resposta:
            botao.config(state="disabled")

        if resultado:
            mensagem = "Resposta correta! Você ganhou pontos."
        else:
            mensagem = "Resposta incorreta!"

        texto = tk.Label(
            self.janela,
            text=mensagem,
            font=("Arial", 12, "bold")
        )
        texto.pack(pady=15)

        proximo = tk.Button(
            self.janela,
            text="Próxima pergunta",
            command=self.avancar
        )
        proximo.pack(pady=10)

    def avancar(self):
        if self.quiz.proxima_pergunta():
            self.mostrar_pergunta()
        else:
            self.mostrar_resultado()

    def mostrar_resultado(self):
        self.limpar_tela()

        jogador = self.quiz.jogador

        titulo = tk.Label(
            self.janela,
            text="FIM DO QUIZ!",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=30)

        nome = tk.Label(
            self.janela,
            text=f"Jogador: {jogador.nome}"
        )
        nome.pack(pady=5)

        pontos = tk.Label(
            self.janela,
            text=f"Pontuação: {jogador.consultar_pontuacao()}"
        )
        pontos.pack(pady=5)

        acertos = tk.Label(
            self.janela,
            text=f"Acertos: {jogador.acertos}"
        )
        acertos.pack(pady=5)

        botao = tk.Button(
            self.janela,
            text="Jogar novamente",
            command=self.mostrar_tela_inicial
        )
        botao.pack(pady=20)