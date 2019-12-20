def jogar_forca():
    print("***********************************************")
    print("*****BEM VINDO AO JOGO DA FORCA!*****")
    print("***********************************************")
    print("Jogando forca")

    palavra_secreta = "banana".upper()  # indifere letra maiscula de minuscula
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = input("Chute a letra:  ")
        chute = chute.strip().upper()  # Tratar espaços digitados pelo usuário e letra maiscula
        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou !")
    else:
        print("Você perdeu, fim do jogo :(")

    print("Fim do jogo !")


if __name__ == "__main__":
    jogar_forca()
