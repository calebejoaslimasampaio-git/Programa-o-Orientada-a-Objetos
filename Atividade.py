# ## Atividade de POO em python do dia 15/10/26
#
# ## 1 Questão
# class veiculo:
#     total_veiculos = 0
#     def __init__(self, marca, modelo,ano):

#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

#         veiculo.total_veiculos += 1

#     def descricao(self):
#         print('A descrisão do veiculo é:')
#         print(f'A marca é: {self.marca}')
#         print(f'A modelo é: {self.modelo}')
#         print(f'A ano é: {self.ano}')
    

# print('cadastrando veiculo...')

# marca_user = input('Insira a marca de seu carro \n -->')
# modelo_user = input('Insira o modelo de seu carro \n -->')
# ano_user = input('Insira o ano de fabricação de seu carro \n -->')


# meu_veiculo = veiculo(marca_user,modelo_user,ano_user)
# print('Resultados:')
# # print(f'A descrição é: {meu_veiculo.descricao()}')
# print(f'O total de veiculos é: {veiculo.total_veiculos}')


# ##2 Questao


# class aluno:

#     def __init__ (self,nome,matricula,nota_final):
#          self.nome = nome
#          self.matricula = matricula
#          self.nota_final = nota_final


#     def exibir_dados(self):
#         print(f"O nome do(a) aluno(a) é: {self.nome}")
#         print(f"A matrícula do(a) aluno(a) é: {self.matricula}")
#         print(f"A nota final do(a) aluno(a) é: {self.nota_final}")
              
#     def verificar_aprovacao(self):
#         if self.nota_final >= 6:
#             print("Aprovado,Se mantenha assim")
#         else:
#             print('Reprovado, se dedique mais no próximo bimestre')



# aluno1 = aluno('Calebe',90028922,10)
# aluno1.exibir_dados()
# aluno1.verificar_aprovacao()





# ##Questão 3

# class livro:
#     def __init__(self, titulo, autor):
#         self.titulo = titulo
#         self.autor = autor
#         self.disponivel = True

#     def emprestar(self):
#         if self.disponivel:
#             self.disponivel = False
#             print(f"O Livro {self.titulo} do autor {self.autor} foi adquirido para emprestimo com sucesso")
#         else:
#             print(f" O Livro {self.titulo} do autor {self.autor} está indisponivel no momento")

#     def devolver(self):
#        self.disponivel = True
#        print(f'O Livro {self.titulo} do autor {self.autor} foi devolvido com Sucesso')


# livro1 = livro('Dom Casmurro', 'Machado de Assis')
# livro1.emprestar()
# livro1.devolver()
        



# ##Questão 4

# class cartaoEstudante:
#     def __init__(self,nomeAlu):
#         self.nomeAlu = nomeAlu
#         self.saldo = 0

#     def recarga(self):
#         print(f' Seja bem vindo {self.nomeAlu}!!')
#         self.saldo = int(input('Qual o valor da recarga \n -->'))
#         print(f'Recarga do aluno {self.nomeAlu} feita com Sucesso, Seu saldo Atual é de {self.saldo}')

#     def usar_passagem(self):
#         tarifa = 2.15
#         if self.saldo >= tarifa:
#             self.saldo -= tarifa
#             print('Passe Aprovado, Catraca liberada ')
#         else: 
#             print('Saldo Insuficiente, recarregue e passe novamente')
#     def consultar_saldo(self):
#         print(f'O Saldo do Aluno:{self.nomeAlu} é de R${self.saldo}.')

# aluno1 = cartaoEstudante('Calebe')
# aluno1.recarga()
# aluno1.usar_passagem()
# aluno1.consultar_saldo()


