import advinhacao
import forca

print("***********************************************")
print("BEM VINDO A ESCOLHA DOS JOGOS!")
print("***********************************************")

escolha = int(input("Qual jogo desejado? \n"
                    "1 - Adivinhação \n"
                    "2 - Forca"))
if escolha == 1:
    advinhacao.escolha_dificuldade()
elif escolha == 2:
    forca.jogar()

