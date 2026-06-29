from random import randint

#  Exercício 07
# Dado o código Python abaixo, você deve estende-lo para adicionar cada 
# uma das funcionalidades descritas abaixo:


# Crie uma lista com 100 elementos contendo números inteiros aleatórios entre 1 e N

lista = []

n = int(input("Digite quantas elementos terá na lista: "))

for _ in range(n):
    lista.append(randint(1,100))

print(lista)

# Calcule e imprima qual é o maior e o menor elemento desta lista

lista.sort()

print(" --------------- lista do maior---------------- ")
print(lista[-1])

print(" --------------- lista do menor ---------------- ")

print(lista[0])

# Copie a lista que você gerou para outra lista, mas contendo apenas os números maiores do que N/2


# lembrar que a lista já está ordenada do maior para o maior, dessa forma só fornecer o número maior que 50 pra cima
print(len(lista))

lista2=lista[50:]

# Limpe a lista original

lista.clear()

# Selecione um item de uma posição aleatória da lista e o remova
valor1 = lista2.pop(10)
print(valor1)

# Calcule e imprima qual é o segundo maior e o segundo menor elemento desta lista

print(list(valor1[-2]))
print(list(valor1[1]))


