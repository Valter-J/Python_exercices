# Papel 10: Organizador
# Exemplo
# Por exemplo, uma lista


from random import randint

lista= []


for a in range(20):
    lista.append(randint(1,100))


# Oganizador

def organizarLista(lista):

    lista.sort()

    print(lista)
    return

print(f"lista antes {lista}")

organizarLista(lista)

print(f"lista depois {lista}")

# Papel 11: Iterador
# Exemplo
# "Escreva um programa que dada uma lista contendo 10
# elementos aleatórios, imprima estes elementos


lista2= []

for a in range(1, 11):
    lista2.append(randint(1,100))


for i in lista2:
    print(f"Lista item por item {i}")