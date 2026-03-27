class Conta:
    def __init__(self):
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor <0:
            raise ValueError("Saldo não pode ser negativo!")
        self.__saldo = valor




    def depositar(self):
        valor = float(input("Digite o valor para depositar: "))
        
        if valor <= 0:
            raise ValueError("Depósito inválido! Valor deve ser maior que zero.")
            
        self.__saldo += valor
        print(f"Depósito de {valor:.2f} realizado com sucesso!")
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Saque inválido! Valor deve ser maior que zero")

        if valor > self.__saldo:
            print("Saldo insuficiente!")
            print(f"Seu saldo atual é R$: {self.saldo:.2f}")
            return
        
        self.__saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

    
    def ver_saldo(self):
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

conta = Conta()



while True:
    print("Bem-Vindo")
    operacao = input("Digite a operação:\n" \
    "1 - SACAR:\n" \
    "2 - DEPOSITAR:\n" \
    "3 - VER SALDO:\n" \
    "0 - SAIR:\n")

    if operacao == "1":
        valor = float(input("Digite o valor que deseja sacar: "))
        conta.sacar(valor)
    elif operacao == "2":
        conta.depositar()
    elif operacao == "3":
        conta.ver_saldo()
    else:
        print("Finalizando....")
        break