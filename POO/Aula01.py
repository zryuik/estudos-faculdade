#ex1

# class Cubo:
#     def __init__(self, valor): #metodo de construtor da classe
#         self.x = valor #atributo
#         print("Metodo Criado Com Sucesso ")
    
#     def calcularcubo(self):
#         cubo = self.x * self.x * self.x
#         return f"Cubo calculado  com sucesso o valor do cubo é {cubo}"
    
# valor = float(input("Digite um Valor para Calcular o cubo: "))
# cubo = Cubo(valor)
# calculo = cubo.calcularcubo()
# print(calculo)

#ex2

#Procedural

# marca = "Toyota"
# modelo = "Corolla"
# ano = 2020

# def exibir(marca, modelo, ano):
#     print(f"O carro da marca {marca}, modelo: {modelo} é do ano: {ano}")

# exibir(marca,modelo,ano)

#POO

# class Carro:

#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

#     def exibir(self):
#         print(f"O carro da marca {self.marca} modelo: {self.modelo} é do ano {self.ano}")

# carro1 = Carro("Toyota" , "Corolla", 2020)
# carro2 = Carro("Volkswagem" , "Gol" , 2012)
# carro3 = Carro("Volvo" , "Penta" , 2025)

# carro1.exibir()
# carro2.exibir()
# carro3.exibir()

#Tentando da Maneira Procedural

# nome = input("Digite seu nome: ")
# venda = float(input("Digite o valor de venda: "))
# meta = 500

# if venda >= meta:
#     print(f"O vendedor {nome} bateu a meta. ")
# else:
#     print(f"O vendedor {nome} nao bateu a meta. ")

class Vendas():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas >= meta:
            print(f"{self.nome} bateu a meta, Parabens!")
        else:
            print(f"{self.nome} não bateu a meta e sera demitido!")

vendedor1 = Vendas("Matheus")
vendedor2 = Vendas("Prof. Thiago")

vendedor1.vendeu(499) 
vendedor2.vendeu(1000)

vendedor1.bateu_meta(500)
vendedor2.bateu_meta(500)