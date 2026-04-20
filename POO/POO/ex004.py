# Classe Conta Bancária

# Crie uma classe Conta com atributo titular e saldo começando em 0
# Método depositar(valor) — soma o valor ao saldo e imprime o novo saldo
# Método sacar(valor) — subtrai se o saldo for suficiente, senão imprime "Saldo insuficiente"
# Método ver_saldo() — imprime o saldo atual
# Crie uma conta, faça 2 depósitos e 1 saque e veja o saldo

class Conta():
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")
        
    def sacar(self, valor):
        if self.saldo  >= valor:
            self.saldo -= valor
            print(f"Saque de R$:{valor} realizado. Saldo atual: {self.saldo}") 
        else:
            print("Saldo insulficiente.")

    def ver_saldo(self):
        
        return f"Saldo Atual de {self.titular}: R${self.saldo}"
    

c1 = Conta("Yure")
c1.depositar(500)
c1.depositar(300)
c1.sacar(200)
c1.ver_saldo()