class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def exibir(self):
        print(f"{self.nome} -> R$: {self.preco}")

produto1 = Produto("Mouse Gamer", 150.0 )
produto2 = Produto("Monitor Gamer", 1400.0)

produto1.exibir()
produto2.exibir()