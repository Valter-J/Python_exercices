# Papel 6 
# Programa exemplo
# "Crie uma lista com 100 números aleatórios. Percorra esta lista e imprima"
# " a posição e o valor do primeiro elemento contido na lista que seja par,"
# " e a posição e o valor do elemento imediatamente após este elemento."

from random import randint

lista=[]

n = int(input("Digite quantas elementos terá na lista: "))

for _ in range(n):
    lista.append(randint(1,100))

print(lista)

for a in lista:

    if (a % 2 == 0):

        posicao = lista.index(a)
        aposPosicao = posicao + 1
        aposPosicaoValor= lista[aposPosicao]

    print(f"Valor do primeiro numero par: {a} , sua posição {posicao}, O valor do item após o primeiro {aposPosicaoValor} e sua posição é {aposPosicao}")





