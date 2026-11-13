#Parte do cadastro Atividade de Importação da aula de reutilização de codigos do dia 05/11
import validacoes
email = input('Insira seu e-mail: \n --> ')
senha = input('Insira sua senha: \n --> ')

if validacoes.verificar_email(email) and validacoes.verificar_senha(senha):
    print('cadastro realizado com sucesso')
else:
    print('cadastro invalido')    