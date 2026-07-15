# Papel 9: Organizador
# Exemplo
# "Escreva um programa que ordene os valores contidos em
# uma lista com 10 elementos -- sem utilizar sort()!"

from random import randint

lista=[]

for _ in range(1,10):
    lista.append(randint(1, 50))

print(lista)

lista2=[]

for i in lista:
    
    inserir = False 
    
    for a in range(len(lista2)):
        valor = lista2[a]
        if ( i < valor):
            lista2.insert(a, i)
            inserir = True
            break
        
    if inserir == False:
        lista2.append(i)
            
        


print(lista)
print (lista2)