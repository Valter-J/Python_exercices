# Papel 9: Organizador
# Exemplo
# "Escreva um programa que ordene os valores contidos em
# uma lista com 10 elementos -- sem utilizar sort()!"

from random import randint

lista=[]

for _ in range (10):
    lista.append(randint(1, 50))

print(lista)

lista2=[]

for i in lista:

    verificador=i

    if (i >= verificador):
        lista2.append(i)
    else:
        contador= lista2.index(i)
        lista2.insert(contador - 1, i)


print(lista)
print (lista2)