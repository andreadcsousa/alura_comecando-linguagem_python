# Onde foi que ela errou?
minha_idade = 26
idade_namorado = 25

if (minha_idade == idade_namorado)
print('temos idades iguais')
else:
    print('temos idades diferentes')

# Faltou o sinal de dois pontos no final da linha do if.


# Comparação estranha
numero1 = 10
numero2 = 10

if (numero1=numero2):
    print("São números iguais")

# Para realizar comparação, deve-se utilizar o sinal de igual duas vezes.


# O resultado da soma é...
idade1 = 10
idade2 = "20"

print(idade1 + idade2)

# O problema aqui é que a "idade2" é um texto, então a soma não acontecerá.

idade1 = 10
idade2 = int("20")

print(idade1 + idade2)

# Como o Python não soma número e texto, precisa converter antes.


# E o resultado agora?
nome = "Nico"
sobrenome = "Steppat"

print(nome + sobrenome)

# O resultado é a soma dos valores sem separação. Usa-se o sep=" " para isso.
