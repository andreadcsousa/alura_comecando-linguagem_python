# Dividindo pontos
pontos_perdidos = abs(chute - numero_secreto)       # pontos perdidos da rodada
# subtraindo os pontos perdidos da pontuação total
pontos = pontos - pontos_perdidos

pontos_perdidos = abs(chute - numero_secreto) / 3   # dividindo por três
pontos_perdidos = abs(21 - 32) / 3                  # dividindo por três
pontos_perdidos = 11 / 3

# O resultado é uma dizima periódica "3.6666666666666665" do tipo float.

pontos_perdidos = 11 / 3
type(pontos_perdidos)       # resultado <class 'float'>

pontos_perdidos = round(11 / 3)

# Para arredondar o valor, utiliza-se a função "round()" e isso retorna 4 como resultado.
