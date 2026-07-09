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


