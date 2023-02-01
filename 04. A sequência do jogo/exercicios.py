# Resultado do programa
contador = 1

while (contador <= 10):
    print(contador)
    contador = contador + 2
    if (contador == 5):
        contador = contador + 2

# O contador irá imprimir 1, somar 2, imprimir 3, somar 2 duas vezes, imprimir 7, somar 2, imprimir 9


# Testando formatação
dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017

"Em 2017 o Carnaval acontece em fevereiro do dia 24 até o dia 28"

# Utilizando o format para inserir variáveis na string acima, teremos:
"Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(
    ano, mes, dia_ini, dia_fim)
