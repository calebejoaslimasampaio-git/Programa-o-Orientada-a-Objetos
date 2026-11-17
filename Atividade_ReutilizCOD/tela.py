#Exemplo do JL
#Aula de continução do tkinter dia 13/11
import tkinter as tk
import validacoes as val

#criando a janela
janela = tk.Tk()

janela.title("Sistema de Cadastro")
janela.geometry("600x500")
janela.configure(bg="darkgray")

#titulo
titulo = tk.Label(
    janela,
    text = "criar conta",
    font = ('Arial',15),
    bg="darkgray",
    fg="black"
)
titulo.pack(pady=15)

#Email
texto_email = tk.Label(janela, text="Email:",bg="darkgray",fg="black")
texto_email.pack()

campo_email = tk.Entry(janela,fg="black")
campo_email.pack()

#senha
texto_senha = tk.Label(janela, text="Senha:",bg="darkgray",fg="black")
texto_senha.pack()

campo_senha = tk.Entry(janela, show="*",fg="black")
campo_senha.pack()

#confirmar senha
texto_confirmar = tk.Label(janela, text="Confirmar Senha:",bg="darkgray",fg="Black")
texto_confirmar.pack()

campo_confirmar = tk.Entry(janela,show="*",fg="black")
campo_confirmar.pack()

#Resultado
resultado = tk.Label(janela,text="",bg="darkgray",fg="black")
resultado.pack()

#Genero
texto_genero = tk.Label(janela,text="Selecione seu genero", bg="darkgray",fg="black")
texto_genero.pack(pady=(10,5))

genero = tk.StringVar(value="")
opcoes_genero1 =[
    "masculino",
    "Feminino"
]
opcoes_genero2 =[
    "Outro",
    "Prefiro não informar"
]

frame_genero = tk.Frame(janela, bg="darkgray")
frame_genero.pack()

coluna_esquerda = tk.Frame(frame_genero, bg="darkgray")
coluna_esquerda.pack(side="left", padx=15, anchor="n")



for opcao in opcoes_genero1:
    tk.Radiobutton(
        coluna_esquerda,
        text=opcao,
        variable=genero,
        value=opcao,
        bg="darkgray",
        fg="black",
        activebackground="darkgray",  # Mantém a cor ao clicar
        selectcolor="white"           # Cor da bolinha selecionada
    ).pack(anchor="w")

# 3. Coluna da direita (empilha Outro e Prefiro não informar)
coluna_direita = tk.Frame(frame_genero, bg="darkgray")
coluna_direita.pack(side="left", padx=15, anchor="n")

for opcao in opcoes_genero2:
    tk.Radiobutton(
        coluna_direita,
        text=opcao,
        variable=genero,
        value=opcao,
        bg="darkgray",
        fg="black",
        activebackground="darkgray",
        selectcolor="white"
    ).pack(anchor="w")


janela.mainloop()