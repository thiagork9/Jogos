import random

def jogo_adivinhacao(tentativas, num_secreto):
    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        num_chute = int(input("Digite seu chute: "))
        print("O seu chute foi", num_chute)

        if num_chute < 1 or num_chute > 100:
            print("Digite um número entre 1 e 100")
            continue

        if rodada >= tentativas:
            print("VOCÊ PERDEU :(")
            print("O número secreto era", num_secreto)
            exit()
        if num_chute == num_secreto:
            print("Você acertou :)")
            exit()
        elif num_chute < num_secreto:
            print("Dica! \n"
                  "Digite um número mais alto")
        elif num_chute > num_secreto:
            print("Dica! \n"
                  "Digite um número mais baixo")


def escolha_dificuldade():
    print("***********************************************")
    print("*****BEM VINDO AO JOGO DA ADIVINHAÇÃO!*****")
    print("***********************************************")
    dificuldade = int(input("Digite a dificuldade desejada: \n"
                            "(1) - Fácil (2) - Normal (3) - Difícil "))
    if dificuldade == 1:
        num_secreto = random.randrange(1, 11)  # gerando de 1 a 10
        tentativas = 6
        jogo_adivinhacao(tentativas, num_secreto)
    elif dificuldade == 2:
        num_secreto = random.randrange(1, 31)  # gerando de 1 a 30
        tentativas = 3
        jogo_adivinhacao(tentativas, num_secreto)
    elif dificuldade == 3:
        num_secreto = random.randrange(1, 101)  # gerando de 1 a 100
        tentativas = 1
        jogo_adivinhacao(tentativas, num_secreto)


if __name__ == "__main__":
    escolha_dificuldade()
