class Motor:
    def Ligar(self):
        print("Ligando motor na base....")

class Carro():
    def __init__(self):
        self.motor = Motor()

    def Ligar(self):
        self.motor.Ligar()
        print("Ligando Motor... ")


#Se fosse herança = Todo carro "É um Motor" = Acoplado
#Sendo composição = Todo carro "Tem um Motor" = Desacoplado


fiat = Carro()
fiat.Ligar()



class Pagamento:
    def pagar(self, valor):
        print(f"Pagamento de R$:{valor}")

class PagamentoPromessa(Pagamento):
        pass

class PagamentoCartao(Pagamento):
        def pagar(self,valor):
            print(f"Pagamento de R${valor} feito no cartão")
    
class PagamentoPix(Pagamento):
        def pagar(self, valor):
            print(f"Pagamento de R$:{valor} feito no PIX")
        

def realizarPagamento(meio, valor):
    meio.pagar(valor)

promessa = PagamentoPromessa()
cartao = PagamentoCartao()
pix = PagamentoPix()

realizarPagamento(promessa, 150)
realizarPagamento(cartao, 1500)
realizarPagamento(pix, 30)
