# Papel 7: Flag de sentido único
# Programa exemplo
# "Escreva um programa que, dada uma lista de elementos, "
# "diga se existe pelo menos um número negativo dentro desta lista."

from random import randint

lista=[]

for _ in range (10):
    lista.append(randint(-10,10))

print(lista)

for i in lista:

    if (i < 0):
        print(f"Exite o numero negativo e esse número é {i}")
    else:
        print(i)
    
    