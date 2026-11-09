#Parte de verificação Atividade de Importação da aula de reutilização de codigos do dia 05/11
def verificar_email(email):
    if "@gmail.com" in email:
        return True
    else:
       return False
def verificar_senha(senha):
    if len(senha) >= 6:
        return True
    else:
        return False
