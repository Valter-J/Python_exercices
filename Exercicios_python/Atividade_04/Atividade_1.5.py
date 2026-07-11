# Papel 8: Temporário
# Exemplo
# "Escreva um programa que inverta os valores contidos em uma lista
# com 10 elementos -- sem utilizar reverse()!"

from random import randint

lista=[]

for _ in range (10):
    lista.append(randint(1, 10))

print(lista)

lista2 =[]

for i in range(-1, -11, -1):
    lista2.append(lista[i])


print(lista2)