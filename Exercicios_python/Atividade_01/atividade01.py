# Questão 1.1
# Você pode usar um nome de variável em uma expressão,
# portanto, faz sentido que você também possa
# usar uma variável para inicializar outra variável.
# Com o seu programa seguinte estado
# Qual o valor armazenado na variável numero2?


numero1 = 100
numero2 = 1 + numero1


print(numero2)


# Questão 1.2
# Você pode copiar o valor de uma variável para outra:
# Qual o valor armazenado na variável numero3?


numero1 = 100
numero2 = 1 + numero1
numero3 = numero2
 
print(numero3)




# Questão 1.3
# Você também pode utilizar uma variável como parâmetro
# de um comando. O que o comando abaixo irá imprimir no console?


numero1 = 100
numero2 = 1 + numero1
numero3 = numero2
print(numero3 - numero2)


# Questão 1.4
# Considerando o comando da linha 5 no programa abaixo


numero1 = 100
numero2 = 1 + numero1
numero3 = numero2
print(numero3 - numero2)
algumaCoisa = numero3 * (numero1 - 10)


print(algumaCoisa)


# opcões verdadeiras
# 1 - Ela define uma nova variável
# 3 - O comando instrui o computador a determinar o valor de uma variável
# 4 - O comando instrui o computador a armazenar um dado em uma variável
# 5 - O resultado intermediário produzido ao avaliar a expressão intermediária numero1 - 10 também será armazenado em uma variável
# 6 - Essa linha de código possui exatamente uma expressão




# Exercício 02
# Organize as linhas de código abaixo de forma que o programa resultante execute,
#  em ordem, os seguintes passos:


minhaConta = 12334
meuSaldoNaTela ="CC Saldo: "
x = minhaConta
contaInv = 120000
saldoTotal = minhaConta + contaInv
print(meuSaldoNaTela + str(saldoTotal))




#Exercício 03
# Escreva um programa em Python que execute todos os seguintes passos:


populacaoNA = 45000
fraseNA = "Nova Andradina tem a população de "
populacaoIV = 40000
popTotal = populacaoNA + populacaoIV
fraseTotal = fraseNA + str(populacaoNA) + " Ivinhema a população de " + str(populacaoIV) + " e o total de " + str(popTotal )


print(fraseTotal)


