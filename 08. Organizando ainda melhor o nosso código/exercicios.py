# Importação de módulo
import b
import a
print("executando a")   # arquivo a.py
print("executando b")   # arquivo b.py

# arquivo principal.py

# o resultado é o próprio conteúdo dos módulos importados "executando a" e "executando b".


# Importação de módulo um pouco diferente
def executa():              # arquivo a.py
    print("Executando a")


def executa():              # arquivo b.py
    print("Executando b")


# principal.py

# Nada acontecerá, pois os códigos de "a.py" e "b.py" foram definidos dentro de uma função. A importação não executa os códigos automaticamente, é preciso chamar os códigos em principal:

# principal.py

a.executa()
b.executa()


# Um módulo pode se chamar automaticamente?
def executa():              # arquivo a.py
    print("Executando a")


">>> python a.py"

# Para chamar um módulo dentro e fora do arquivo com uma função "def" declarada
# É preciso criar uma condição com uma variável que chame a função e ela execute


def executa():
    print("Executando a")


if (__name__ == "__main__"):
    executa()
