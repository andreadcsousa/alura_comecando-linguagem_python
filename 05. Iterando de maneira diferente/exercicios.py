# De while para for
contador = 1
while (contador <= 10):
    print(contador)
    contador = contador + 1

# Para substituir o while pelo for, pode-se utilizar a função range juntamente com ele, sem necessidade do incremento:
for contador in range(1, 11):
    print(contador)


# De while para for #2
contador = 1
while (contador <= 10):
    print(contador)
    contador = contador + 3

# O contador acima imprime 1, 4, 7, 10. Substituindo while por for, fica assim:
for contador in range(1, 11, 3):
    print(contador)


# break e continue
"break sai do bloco do laço abruptamente"
"continue apenas pula para próxima iteração"


# while com break
i = 1
while (i <= 7):
    print(i)
    i = i + 1
    if (i == 5):
        break

# O programa vai imprimir: 1, 2, 3, 4. Ele soma de 1 em 1 e quando chega no 5 ele para, pois a repetição para antes de imprimir o valor.


# for com continue
for i in range(1, 8):
    if (i == 5):
        continue
    print(i)

# O programa irá imprimir: 1, 2, 3, 4, 6, 7. Ele pula o número 5 e continua a partir daí. Enquanto que o número 8 não é exibido por causa do range.


# Adaptando o padrão americano
print("Ola Sr.{1} {0}".format("Cordeiro", "Leonardo"))

# Ao declarar a variável na string, basta escolher o valor correspondente na ordem correta.
# Lembrando que a contagem começa em 0 (zero), como no JavaScript.


# O resultado da interpolação
"R$ {:7.1f}".format(1000.12)
"R$ {:07.2f}".format(4.11)

# Imprime, respectivamente: "R$ 1000.1" e "R$ 0004.11", podendo até arredondar em alguns casos.
# Exemplo 1: São 7 casas inteiras e 1 casa decimal.
# Exemplo 2: São 7 casas inteiras e 2 casas decimais e zeros à esquerda.


# Recurso "f-strings" ou formatted strings literals
nome = 'Matheus'
print(f'Meu nome é {nome}')

"Meu nome é Matheus"
