# Faixa etária
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade < 12):
        print("Você é uma criança.")
    elif (idade > 12):
        print("Você é um adolescente.")

# 12 não é maior que 18, não é menor que 12 e não é maior que 12. então o número 12 não está sendo testado. Nesse caso, deve substituir o sinal de "<" e ">" por "<=" e ">=".


# Faixa etária - variáveis
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
crianca = idade < 12
adolescente = idade > 12

# Ao digitar 15 anos, será retornado que "maior_idade" e "crianca" são falsos e "adolescente" é verdadeiro.


# If...else... e nada funciona
usuario = input("Informe o usuário do sistema!")

if (usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
else (usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
else (usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")

# Deve-se substituir os "else" das linhas 34 e 36 por "elif" para que sejam validados os demais usuários.


# Qual é o tipo?
acertou = (chute == numero_secreto)

# A variável "acertou" é do tipo booleana, pois só aceita verdadeiro ou falso como valor.


# Para saber mais: if sem ou com parênteses?
if (acertou):
    print("Parabéns! Você acertou.")

if acertou:
    print("Parabéns! Você acertou.")

# Os parênteses não são obrigatórios, porém para deixar claro qual é a condição, utiliza-se assim mesmo.
