# Classe Pessoa
# Crie uma classe Pessoa com os atributos nome e idade
# Crie um método apresentar() que imprima uma apresentação formal
# Crie um objeto p1 com seu nome e idade e chame apresentar()

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e minha idade é {self.idade} anos")

pessoa1 = Pessoa("Yure", 25)

pessoa1.apresentar()