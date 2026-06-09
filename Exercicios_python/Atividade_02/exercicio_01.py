# Exercício 01
# Organize as linhas de código abaixo de forma que o programa resultante que solucione o seguinte problema:


numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
mult = numero1 * numero2
print(mult)


# Crie uma variável chamada populacaoNA que armazena um valor qualquer inserido pelo usuário.
# Crie uma variável chamada fraseNA que armazena a expressão String "Nova Andradina tem a população de X", sendo X substituído pelo valor armazenado na variável populacaoNA
# Crie uma variável chamada populacaoIV que armazena qualquer valor qualquer inserido pelo usuário
# Crie uma variável chamada popTotal que armazena o valor populacaoNA + populacaoIV
# Crie uma variável chamada fraseTotal que armazena a expressão String "Nova Andradina tem a população de X, Ivinhema a população de Y e o total de Z", sendo que X, Y e Z devem ser substituídas pelos valores das variáveis populacaoNA, populacaoIV e popTotal
# Imprima no console as variáveis fraseNA e fraseTotal

populacaoNA = int(input("Digite o numero da população"))
fraseNA = "Nova andradina tem população de " + str(populacaoNA)
populacaoIV = int(input("Digite o valor da polulação IV"))
popTotal = populacaoNA + populacaoIV

fraseTotal = (
    "Ivinhema a população de " + str(populacaoIV) + "e o total de " + str(popTotal)
)

print(fraseNA, fraseTotal)


# Exercício 03
# Escreva um programa em Python que solucione o seguinte problema:
# Crie uma calculadora que aceita como entrada três números quaisquer, calcule a soma do primeiro número com o segundo número e multiple
# o resultado da soma pelo terceiro número, apresentando este valor como resultado final.


calnumb1 = int(input("Digite o 1º da cal"))
calnumb2 = int(input("Digite o 2º da cal"))
calnumb3 = int(input("Digite o 3º da cal"))

calnumb1 = calnumb1 + calnumb2

calnumb1 = calnumb1 * calnumb3
print(calnumb1)


# Exercício 04
# Reflita sobre o seguinte programa em Python:

prim = 20
sec = 10

if prim < sec:
    prim = prim / 2
if prim < 2 * sec:
    prim = prim * 2
    sec = sec / 2
else:
    prim = prim + 1
    sec = sec - 1

elasSaoIguais = prim == sec

if elasSaoIguais:
    prim = prim + 1

print(prim, sec)



