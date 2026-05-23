# Python não exige declarar tipo da variável
# Em linguagens como C, Java e C++ você precisa definir o tipo




# testando python

print(" Testando o programinha python, vamos fazer um pequeno programa para testar")

nome = input("Primeiro, digite seu nome: ")
idade = int(input("digite sua idade: "))
altura = float(input("digite sua altura: "))

if idade > 18 :
    print("Seu nome é"+ nome + ", voce tem " + str(altura) + "e você é maior de idade" )
else:
    print("Seu nome é"+ nome + ", voce tem " +  str(altura) + "e você e você é menor de idade")