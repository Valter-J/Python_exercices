# Papel 05
# Programa exemplo
# Escreva um programa que leia 10 números inteiros, os armazene em uma lista e posteriormente 
# calcule a soma de todos os elementos da lista.


numero = []

for i in range(1, 11):
  numero.append(int(input("Digite um numero de 0 a 100: ")))
  soma = 0

  for a in numero:
    soma = soma + a



print("------------resultado-----------")
print(numero)
print(soma)