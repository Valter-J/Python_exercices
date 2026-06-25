#  Exercício 07
# Dado o código Python abaixo, você deve estende-lo para adicionar cada 
# uma das funcionalidades descritas abaixo:


# Crie uma lista com 100 elementos contendo números inteiros aleatórios entre 1 e N
# Calcule e imprima qual é o maior e o menor elemento desta lista
# Copie a lista que você gerou para outra lista, mas contendo apenas os números maiores do que N/2
# Limpe a lista original
# Selecione um item de uma posição aleatória da lista e o remova
# Calcule e imprima qual é o segundo maior e o segundo menor elemento desta lista

from random import randint

lista = []

n = int(input("Digite quantas elementos terá na lista: "))

for _ in range(n):
    lista.append(randint(1,100))

print(lista)

