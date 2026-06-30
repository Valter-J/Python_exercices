# Exercício 01
# Considere o seguinte programa em Python:

def calcularImposto (renda, rendaMinima,baseCalculo, baseAdicional):
    taxaBasica = min(renda, rendaMinima)
    taxaAdicional = max((renda-rendaMinima), 0)
    return taxaBasica + (taxaAdicional * baseAdicional)


meuImposto = calcularImposto(800, 150, 200, 100)
print(meuImposto)


# Pense neste código em execução. Responda às perguntas abaixo:

# Qual é o valor impresso no console ao final da sua execução?

# reposta : 65150

# As linhas do programa estão numeradas de 1 a 8. Qual a sequência em que essas linhas são executadas?

#  a sequência seria: 1, 6, 1, 2, 3, 4, por último 7. 


# Na linha 2, quanto valem os parâmetros renda, rendaMinima, baseCalculo e baseAdicional?

# renda: 800, rendaMinima: 150, baseCalculo: 200, baseAdicional: 100.  




# Exercício 02

# O programa em Python abaixo deve calcular a média aritmética de três 
# notas e retornar "Aprovado" caso o aluno tenha média superior ou igual a 
# 6, e "Reprovado" caso contrário. O programa está quase pronto, complete
# o código abaixo para que o programa execute a funcionalidade descrita acima:


def calcularMedia ( nota1, nota2, nota3 ):
  media = nota1 + nota2 + nota3/3

  aprovado = media >= 6
  reprovado = media <= 6
  if (aprovado):
     print("Você está aprovado")
  
  
  else:
    print("Você está reprovado")
  
resultadoAluno1 = calcularMedia(3, 6, 9)
print(resultadoAluno1)
resultadoAluno2 = calcularMedia(4,3, 5)
print(resultadoAluno2)