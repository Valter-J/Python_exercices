# Papel 4: O Detentor Mais Procurado
# Programa exemplo "Escreva um programa que leia um 10 "
# "números inteiros e imprima qual é o maior e o menor dos"
# " números lidos"

# Leitura do primeiro número
numero = int(input("Digite o 1º número: "))
maior = numero
menor = numero

# Leitura dos outros 9 números
for i in range(2, 11):
    numero = int(input(f"Digite o {i}º número: "))

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

# Exibição dos resultados
print("Maior número:", maior)
print("Menor número:", menor)


