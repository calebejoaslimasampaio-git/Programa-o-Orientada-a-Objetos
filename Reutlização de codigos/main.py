# Explicação da aula de reutilização de codigos do dia 05/11
import calculos
preco_produto = 100.00

#usando as funções do móddulo
preco_com_desconto = calculos.calcular_desconto(preco_produto, 15)
imposto = calculos.calcular_imposto(preco_produto)

print(f'preço com desconto: R${preco_com_desconto:.2f}')
print(f"Imposto: R$ {imposto:.2f}")