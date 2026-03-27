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
        print(f"Depósito de {valor:.2f}realizado com sucesso!")
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Saque inválido! Valor deve ser maior que zero")

        if valor > self.__saldo:
            print("Saldo insuficiente!")
            return
        
        self.__saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

    
    def ver_saldo(self):
        print(f"Saldo atual: R$ {self.__saldo:.2f}")
