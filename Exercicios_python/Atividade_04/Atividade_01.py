# Papel 1

# "Escreva um programa que armaze o endereço do servidor
#  e o caminho para conexão do banco de dados de forma
#  que esta informação não poderá ser posteriormente
#  alterada dentro do programa."



SERVIDOR = "LOCALHOST:8080/"
SENHA = "ROOT"



# Papel 2: Passo
# Programa exemplo
# "Escreva um programa que imprima a taboada de um número n qualquer"


n = int(input("Digite um número"))

for base in range(1,11):
    print(str(n) + "x" + str(base) + "=" + str(base * n))



# Papel 3: O Detentor Mais Recente
# Programa exemplo
# "Escreva um programa que leia um número e o ensira em uma lista. 
# A inserção de valores termina quando o usuário digitar um número negativo."




x = int(input("Digite um número para criar a lista"))

x= [x*x for x in range(13)]
for imprimi in x:
    print(imprimi)

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

