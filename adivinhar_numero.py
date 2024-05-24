import random


def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("Bem-vindo ao jogo de adivinhar o número!")
    print("Estou pensando em um número entre 1 e 100.")

    while not acertou:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Seu palpite é muito baixo.")
        elif palpite > numero_secreto:
            print("Seu palpite é muito alto.")
        else:
            acertou = True
            print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")


if __name__ == "__main__":
    adivinhar_numero()
