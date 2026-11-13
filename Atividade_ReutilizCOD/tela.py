#Exemplo do JL
#Aula de continução do tkinter dia 13/11
import tkinter as tk
import validacoes as val

#criando a janela
janela = tk.Tk()

janela.title("Sistema de Cadastro")
janela.geometry("500x300")

#titulo
titulo = tk.Label(
    janela,
    text = "criar conta",
    font = ('Arial',18)
)
titulo.pack(pady=15)

#Email
texto_email = tk.Label(janela, text="Email:")
texto_email.pack()

campo_email = tk.Entry(janela)
campo_email.pack()

#senha
texto_senha = tk.Label(janela, text="Senha:")
texto_senha.pack()

campo_senha = tk.Entry(janela, show="*")
campo_senha.pack()

#confirmar senha
texto_confirmar = tk.Label(janela, text="Confimar senha")
texto_confirmar.pack()

campo_confirmar = tk.Entry(janela,show="*")
campo_confirmar.pack()

#Resultado
resultado = tk.Label(janela,Text="")
resultado.pack()

#Genero
texto_genero = tk.Label(janela,text="Selecione seu genero")
texto_genero.pack()

genero = tk.StringVar(value="")
opcoes_genero =[
    "masculino",
    "Feminino",
    "Outro",
    "Prefiro não informar"
]
for opcao in opcoes_genero:
    tk.Radiobutton(
        janela,
        text= opcao,
        variable=genero,
        value=opcao
    ).pack(anchor="W")
janela.mainloop()