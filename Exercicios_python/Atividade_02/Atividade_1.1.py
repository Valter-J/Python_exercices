# Escreva um algoritmo que leia as três componentes das notas da disciplina de Construção
# de Algoritmos: sua nota de trabalho, sua nota de atividades e sua nota de participação de prova. 
# Para calcular a média final, considere que a nota de prova corresponde a 50% da nota final, a nota 
# de atividades a 20% e a nota de trabalho a 30% da nota final. Após calcular a média final, o programa
# deve dizer se o aluno está aprovado ou reprovado.

notaProva = float(input("Digite a nota do trabalho"))
notaAtividade = float(input("Digite a nota da atividade "))
notatrabalho = float(input("Digite a nota de participação"))

# Cálculo da média final
media_final = (notatrabalho * 0.30) + (notaAtividade * 0.20) + (notaProva * 0.50)

# Exibição da média
print(f"Média final: {media_final:.2f}")

# Verificação da situação do aluno
if media_final >= 6.0:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

    