from random import randint
#Super Classe ou Classe Pai
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida


    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self.__vida = 0
        elif valor > 100:
            self.__vida =100
            print(f"{self.nome} não pode receber valores de vida acima de 100")
            print(f"Portanto ele possui agora {self.__vida} pontos de vida.")
        else:
            self.__vida = valor

    def atacar(self):
        print(f"{self.nome} realizou um ataque!")

#classe que herda de personagem 

class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.forca = forca

    def atacar(self):
        ataque = self.forca - randint(0, 30)
        print(f"{self.nome} golpeou com a espada causando {ataque} de dano!")
        return max(0, ataque)  #garante que o ataque seja maior que 0

#classe que tambem herda de personagem

class Mago(Personagem):
    def __init__(self, nome, vida, magia):
        super().__init__(nome, vida)
        self.magia = magia

    def atacar(self):
        ataque = self.magia - randint(0, 30)
        print(f"{self.nome} lançou uma magia causando {ataque} de dano!")
        return max(0, ataque)

# #exemplo basico de polimorfismo

# personagens = [
#     Guerreiro("Titan", 150, 35),
#     Guerreiro("Goat", 150, 40),
#     Guerreiro("Levi", 150, 45),
#     Mago("Icarus", 100, 70),
#     Mago("Edthree", 100, 80),
#     Mago("Eyes", 70, 90)
# ]

# #polimorfismo em ação
# for p in personagens:
#     p.atacar() #o método se adapta ao objeto


personagens = []

print("==================== Bem Vindo a Batalha no Terminal ====================")
print("--- Mago ou Guerreiro ---")
print("----------------------------------------------------")

#polimorfismo em ação

for _ in range(0,2):
    classePersonagem = int(input("Digite [1] para - Guerreiro\nDigite [2] - Mago\nR: "))

    nome = input("Digite o nome do Personagem: ")
    vida = int(input(f"{nome} possuirá Vida: "))

    if classePersonagem == 1:
        forca = int(input(f"{nome} possuirá Forca: "))
        jogador = Guerreiro(nome, vida, forca)


    elif classePersonagem == 2:
        magia = int(input(f"{nome} Possuirá Inteligência: "))
        jogador = Mago(nome, vida, magia)

    personagens.append(jogador)
    print("----- Jogador Criado -----")

player1 = personagens[0]
player2 = personagens[1]

print("===== Inicio da Batalha =====")
print(f"{player1.nome} vs {player2.nome}")
print("=============================")

#loop de batalha

while True:
    #turno 1


    escolha = input(f"{player1.nome} deseja atacar ? [S/N]: ")

    if escolha in "sS":
        ataque = player1.atacar() #polimorfismo
        player2.vida -= ataque
        print(f"{player2.nome} agora tem {player2.vida}")
        print("=================")


    else:
        print(f"{player1.nome} passou a vez")


    if player2.vida <= 0:
        print(f"{player2.nome} esta morto! Parabens {player1}, voce venceu a batalha!")
        break

    #turno 2


    escolha = input(f"{player2.nome} deseja atacar ? [S/N]: ")

    if escolha in "sS":
        ataque = player2.atacar() #polimorfismo
        player1.vida -= ataque
        print(f"{player1.nome} agora tem {player1.vida}")
        print("=================")


    else:
        print(f"{player2.nome} passou a vez")


    if player1.vida <= 0:
        print(f"{player1.nome} esta morto! Parabens {player2.nome}, voce venceu a batalha!")
        break
