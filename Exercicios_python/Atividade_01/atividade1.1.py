# Exercicio 4:


areaM2 = 0
cobTinta =20
tintaLit= 0
valLata = 519.00


print("Por favor insira o valor do seu estoque inicial de Tintas em litros")


tintaLit =float(input())


print(" O valor do seu estoque é " + str(tintaLit))


print("Digite o valor da area em m2 a ser pintado")


areaM2 = float(input())
quatlitros = areaM2/20
qtdLatas = (quatlitros // tintaLit)
vendaTinta = qtdLatas * valLata


print("Você precisa de "+ str(qtdLatas) + " litros por m2"+", e o valor total de tinta que você precisará é R$ " + str(vendaTinta) )



# streamlit, python
