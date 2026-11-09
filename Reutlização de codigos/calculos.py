# Explicação da aula de reutilização de codigos do dia 05/11
def calcular_desconto(preco,porcentagem):
    """Calcule o valor final com desconto """
    return preco - (preco * (porcentagem / 100))
def calcular_imposto(preco):
    """calcula imposto padrao de 10%"""
    return preco * 0.10