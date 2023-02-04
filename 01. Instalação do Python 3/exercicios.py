# Treinando a função print
print("Olá, mundo!")

# Modificando o valor do separador
print("Brasil ganhou 5 títulos mundiais", sep=" ")  # padrão
print("Brasil", "ganhou", 5, "títulos mundiais", sep=" ")
print("Brasil", "ganhou", 5, "títulos mundiais", sep="-")
print("Brasil", "ganhou", 5, "títulos mundiais", sep="")

# Modificando o valor do finalizador
print("Brasil ganhou 5 títulos mundiais", end="\n")  # padrão
print("Brasil ganhou 5 títulos mundiais", end="")
print("Brasil ganhou 5 títulos mundiais", end="END")

# Criando variáveis
pais = "Itália"
type(pais)  # imprime <class 'str'>, ou seja, string

quantidade = 4
type(quantidade)  # imprime <class 'int'>, ou seja, inteiro

print(pais, "ganhou", quantidade, "títulos mundiais.")

# Imprimindo datas
dia = 15
mes = 10
ano = 2015

print(dia, mes, ano, sep="/")
