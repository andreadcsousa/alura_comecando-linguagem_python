# importando o módulo random para o jogo
import random

print("*********************************")
print("Bem-vindo ao jogo de Adivinhação!")
print("*********************************")

# definindo o que será sorteado
numero_secreto = random.randrange(1, 101)
total_tentativas = 0
pontos = 1000

# definindo o nível de dificuldade do jogo
print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Digite o nível: "))

# definindo a quantidade sorteada por nível
if (nivel == 1):
    total_tentativas = 20
elif (nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

# sorteando o número secreto e rodando as tentativas
for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))

    # convertendo string em inteiro
    chute_str = input("Digite um número entre 1 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    # reconhecendo o chute digitado pelo usuário
    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 100!")
        continue

    # definindo a resposta do chute x número sorteado
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        # interpolando string para mostrar os pontos de acerto
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
            # ao termino das tentativas, revela o valor do número sorteado
            if (rodada == total_tentativas):
                print("O número secreto era {}. Você fez {}".format(
                    numero_secreto, pontos))
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
            if (rodada == total_tentativas):
                print("O número secreto era {}. Você fez {}".format(
                    numero_secreto, pontos))

        # calcula os pontos dos chutes errados do usuário no jogo
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do jogo.")
