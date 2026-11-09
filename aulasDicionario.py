pessoa = {'nome':'calebe','idade':'15'}
pessoa.update({'cidade' : 'São Paulo'})
print(pessoa)

#Questão 1 Criação e acesso basico

aluno = {'nome':'Ana Souza', 'idade':22,'curso':'Ciência da Computação'}
# #para imprimir todos os termos
for chave,valor in aluno.items():
     print(chave,':',valor)
#ou
#imprime somente o curso e o aluno
print('Nome:',aluno.get('nome'))
print('Curso',aluno.get('curso')) 

#Questão 2 Continuação 18/09

aluno.update({'idade':23})
aluno.update({'semestre':5})

#Printa todos os itens
for chave,valor in aluno.items():
     print(chave,':',valor)

#Questão 3 

precos ={
    'lapis':2.50,
    'caderno':18.00,
    'borracha':1.20,
    'caneta':3.00

}
for produtos,valor in precos.items():
     print(f'O produto {produtos} custa: R${valor}')



