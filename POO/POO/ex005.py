# Classe Funcionário com múltiplos objetos

# Crie uma classe Funcionario com nome, cargo e salario
# Método apresentar() que imprime nome e cargo
# Método dar_aumento(percentual) que aumenta o salário pelo percentual informado
# Método ver_salario() que imprime o salário atual
# Crie 3 funcionários, guarde em uma lista, dê 10% de aumento para todos usando um for, e exiba o salário de cada um

class Funcionario():
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    
    def apresentar(self):
        print(f"Funcionario: {self.nome} - Cargo: {self.cargo}")


    def dar_aumento(self, percentual):
        self.salario += self.salario * (percentual / 100)

    def ver_salario(self):
        print(f"{self.nome} - {self.cargo}: R${self.salario:.2f}")
    

funcionarios = [
    Funcionario("Ana", "QA", 4000),
    Funcionario("Yure", "DEV", 20000),
    Funcionario("Carla", "DBA", 5000)
]

for j in funcionarios:
    j.dar_aumento(10)

for j in funcionarios:
    j.ver_salario()

