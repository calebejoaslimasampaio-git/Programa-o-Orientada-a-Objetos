# class ContaBancaria():
#     def __init__(self, titular, saldo = 0.0):
#         self.titular = titular
#         self.saldo = saldo

#     def depositar(self, valor):
#         if (self.saldo >= 0):
#             self.saldo += valor
#             print(f"Seu novo saldo: {self.saldo}\n")
#         else:
#              print(f"Seu novo saldo: {self.saldo}\n")

#     def sacar(self, valor):
#         if (self.saldo < valor):
#             print("Saldo insuficiente para realizar o saque\n")
#         else:
#             self.saldo -= valor
#             print("Saque realizado com sucesso\n")

#     def extrato(self):
#             print(f"Nome do titular: {self.titular}, saldo: {self.saldo}\n")

# conta1 = ContaBancaria("Ana", 500.00)
# conta1.depositar(200)
# conta1.sacar(900)
# conta1.sacar(150)
# conta1.extrato()