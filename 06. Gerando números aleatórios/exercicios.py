# O menor e o maior
import random

aleatorio = random.randrange(10)
print(aleatorio)

# Com apenas 1 parâmetro o range supõe que vai de zero até o número definido -1. Menor = 0 / Maior = 9.


# Múltiplos aleatórios
int(random.random() * 100)
round(random.random() * 100)
random.randrange(0, 101)
random.randint(0, 101)

# 4 formas de gerar números aleatórios entre 1 e 100


# O grande sorteio
sorteado = random.randrange(0, 4)

print(sorteado)

if sorteado == 1:
    print("Paulo")
elif sorteado == 2:
    print("Juliana")
else:
    print("Tamires")

# Injusto, pois como não tem número associado a Tamires, ela fica com 2 chances de ser sorteada.
# Acontece que 0 e 3 não foram associados a ninguém e as saídas possíveis são 0, 1, 2 e 3.
