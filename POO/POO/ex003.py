# Classe Aluno com média
# Agora você precisa criar um método que faz um cálculo usando os próprios atributos do objeto.

# Crie uma classe Aluno com atributos nome, nota1 e nota2
# Crie um método calcular_media() que calcula a média das duas notas
# Crie um método situacao() que imprime se o aluno foi aprovado (média >= 6) ou reprovado
# Teste com pelo menos 2 alunos — um aprovado e um reprovado

class Aluno():
    def __init__(self,nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        media = self.calcular_media()
        if media >=6:
            print(f"{self.nome} - Aprovado! Média: {media}")
        else:
            print(f"{self.nome} - Reprovado! Média: {media}")

pessoa1 = Aluno("Yure", 8.0, 10.0)
pessoa2 = Aluno("Juse", 5, 4)

pessoa1.situacao()
pessoa2.situacao()