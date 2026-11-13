#Aulas de introducão tkinter 12/11 e 13/11
#Area Import
import tkinter as tk
# import validacoes as v

# 1. Crie a função que o botão vai executar ao ser clicado
def acao_botao():
    nome_digite = caixa_entry.get()
    label_resultado.config(text=f"Bem-vindo,{nome_digite}!")

janela =tk.Tk()
janela.title("Minha primeira janela")
janela.geometry("500x300")

# Título interno (instanciado e posicionado na tela)
titulo = tk.Label(janela, text='Sistema Login', font=('Arial',14,'bold')) 
titulo.pack(pady=10)


#CAIXA E TEXTO DE UMA LINHA(ENTRY)
label_entry = tk.Label(janela,text="Digite Seu nome:")
label_entry.pack(pady=5)
caixa_entry = tk.Entry(janela, width=30)
caixa_entry.pack(pady=5)

# 2. Crie o botão ligando-o à função através do parâmetro 'command'
botao_entrar = tk.Button(janela, text="Entrar", command=acao_botao)
botao_entrar.pack(pady=15)

# Texto vazio que será preenchido após o clique
label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=5)

janela.mainloop()