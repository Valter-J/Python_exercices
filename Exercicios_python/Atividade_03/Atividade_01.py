# Exercícios Listas

# Exercício 01
teste = [4, 10, 3, 10, 15, -2]
algumIndice = 4
valor = teste[2]
print(valor + teste[algumIndice] + teste[4])
# resposta: 33

# Exercício 02
# Examine os comandos abaixo.

teste = [4, 10, 3, 10, 15, -2]
indice = 0
teste[indice] = 0
indice = indice + 1
teste[indice] = 0
indice = indice + 1
teste[indice] = 0
indice = indice + 1
teste[indice] = 0

# Após a execução desses comandos, qual será a soma dos elementos da lista?

# reposta: 13

# TODO: Fazer com o while


# Exercício 03

#Inserindo um elemento na última posição da lista

numeros = [0.1, 2.3, 0, -3.1, 5.0, 7.1, 25.9]

numeros.insert(7,4)

print(len(numeros))
print(numeros[-1])

# Exercício 04

estoque = ["sabão", "amaciante", "detergente", "desinfetante", "sabão em pedra", "limpa vidros"]
estoque.pop()
estoque.pop(0)
estoque.pop()
estoque.pop()
print(estoque)

# Reposta: ['amaciante', 'detergente']

# Exércicio 5

estoque = ["sabão", "amaciante", "detergente", "desinfetante", "sabão em pedra", "limpa vidros"]
elem = "detergente"

#Procurar índice do elemento

indice = estoque.index("amaciante")
print(indice)

#testar se o índice está nos limites da lista



#remover o elemento e imprimir a lista
estoque.pop(0)
print(estoque)

#ou apresentar mensagem de que o elemento não existe.

indice = 6

if 0 <= indice < len(estoque):
    print(estoque[indice])
else:
    print("Indice inválido")
