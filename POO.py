# #1 questão da atividade (slide)

# num1 = int(input('Digite um numero: \n ->'))
# num2 = int(input('Digite outro numero: \n ->'))
# num3 = int(input('Digite um último numero: \n ->'))
# print('Processando....')
# if num1 > num2 and num1 > num3:
#     maior = num1
# elif num2 > num1 and num2 > num3:
#     maior = num2
# elif num3 > num1 and num3 > num2:
#     maior = num3

# if num1 < num2 and num1 < num3:
#     menor = num1
# elif num2 < num1 and num2 < num3:
#     menor = num2
# elif num3 < num1 and num3 < num2:
#     menor = num3

# print (f'O maior numero é: \n -> {maior}')
# print (f'O menor numero é: \n -> {menor}')


# # 2 questão da atividade (slide)
# nome =  input('Informe seu nome: \n -->')
# nota1 = float(input('Diga sua Primeira nota: \n -->'))
# nota2 = float(input('Diga sua Segunda nota: \n -->'))
# media = (nota1 + nota2) / 2

# if media == 10 :
#     print(f'Parabéns {nome} sua média é {media}, continue assim!!')
# elif media >= 7:
#     print(f'Aprovado, sua média é {media}')
# else:
#     print(f'Reprovado {media}, melhore {nome}, você consegue!')

# # 3 questão da atividade
# nome = input('Informe seu nome: \n -->')
# salario = int(input('Informe seu salário: \n -->'))

# if salario <= 280:
#     percentual = 20
#     valor = (salario * (percentual/100)) 
#     novosal = valor + salario

# elif salario < 700 and salario > 280 :
#     percentual = 15
#     valor = (salario * (percentual / 100))
#     novosal = valor + salario

# elif salario >= 700 and salario < 1500:
#     percentual = 10
#     valor = (salario * (percentual / 100))
#     novosal = valor + salario

# elif salario >= 1500:
#     percentual = 5
#     valor = (salario * (percentual / 100))
#     novosal = valor + salario

# print(f'{nome} seu salario antigo era R$ {salario},00 .')
# print(f'O percentual de aumento aplicado ao seu salário foi de {percentual}% .')
# print(f'O valor do aumento foi de  R$ {valor}.')
# print(f'Seu salario atual é de R$ {novosal}.')