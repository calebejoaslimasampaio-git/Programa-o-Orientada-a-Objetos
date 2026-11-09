#criado no dia 24/09(anotações de funcão e metodos )

# def soma(a,b=0):
#     return a+b
# resultado=soma(3,5)
# resultado=soma(3)

# o def sozinho faz uma ação,mas com o __init__ define 
# class controleRemoto:
#     def __init__(self):
#         self.cor='preto'
#         self.altura='10cm'
#         self.profundidade='2cm'
#         self.largura='2cm'
# controle1 = controleRemoto()
# controle2 = controleRemoto()

#pode deixar com que o usuario altere tais atributos(personalização)




# class ControleRemoto:
#     def __init__(self,valor_da_cor,altura,profundidade):
#         self.cor = valor_da_cor
#         self.altura = altura
#         self.profundidade = profundidade
#         self.largura = "2cm"

#     def passar_canal(self,botao):
#         if botao == "+":
#             print ("aumentar o canal")
#         elif botao == '-':
#             print("diminuir o canal")
# controle1 = controleRemoto("preto","0.6","0.6")
# print(controle1.largura)
# controle1.passar_canal("+")

#Aula P.O.O  dia 25

# class dog:
#     def __init__(self):
#         self.nome = input('Escreva Um Nome para o seu cachorro: \n--> ')
#         self.raca = input('Qual será a raça? \n -->')
#         self.truque = input('Qual truque ele fará? \n-->')

       
#     def latir(self):
#             print('Au,Au')
#     def fazerTruque(self):
#             print('O cachorro',self.nome,'está fazendo um', self.truque,'!!')

# meu_cachorro = dog()
# meu_cachorro.latir()
# meu_cachorro.fazerTruque()

#quetão 1

class carro:
    def __init__(self):
        self.marca = input('Qual a marca do seu carro? \n-->')
        self.modelo = input('Qual o modelo do seu carro? \n-->')
        self.cor = input('Qual a cor do seu carro? \n-->')
        self.combustivel = input('Qual o combustivel usado no seu carro? \n-->')

    def ligar(self):
        print(f'O carro ligou')

    def acelerar(self):
        print(f'O carro {self.marca} {self.modelo} {self.cor} acelerou!!')

    def frear(self):
        print(f'O carro {self.marca} {self.modelo} freiouuu!!')


meu_carro = carro()
meu_carro.ligar()
meu_carro.acelerar()
meu_carro.frear()
                
        