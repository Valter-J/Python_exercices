# Exercício 07

# Problema
# Uma empresa concederá um aumento de salário aos seus funcionários, variável 
# de acordo com o cargo, conforme a tabela abaixo. Faça um algoritmo que leia 
# o salário e o cargo de um funcionário e calcule o novo salário. Se o cargo 
# do funcionário não estiver na tabela, ele deverá, então, receber 40% de aumento.
# Mostre o salário antigo, o novo salário e a diferença.


print("Por favor Escolha umas das opções abaixo. ")
print("Digite 1, para gerente. ")
print("Digite 2, para Engenheiro. ")
print("Digite 3, para técnico.")
print("Digite 4, para profissões.")

opcao = int(input())


match opcao:
    case 1:
        
       salario = float(input("Digite seu Salario: "))
       salarioFinal = salario * 1.10
       salarioDiferença = salarioFinal - salario
       print("Seu salário antigo é " + str(salario) + " , seu salario novo é " + str(salarioFinal) + " com diferença de " + str(salarioDiferença))

    case 2:
        
        salario = float(input("Digite seu Salario: "))
        salarioFinal = salario * 1.20
        salarioDiferença = salarioFinal - salario
        print("Seu salário antigo é " + str(salario) + " , seu salario novo é " + str(salarioFinal) + " com diferença de " + str(salarioDiferença))

    case 3:

        salario = float(input("Digite seu Salario: "))
        salarioFinal = salario * 1.30
        salarioDiferença = salarioFinal - salario
        print("Seu salário antigo é " + str(salario) + " , seu salario novo é " + str(salarioFinal) + " com diferença de " + str(salarioDiferença))

    case 4:

        salario = float(input("Digite seu Salario: "))
        salarioFinal = salario * 1.40
        salarioDiferença = salarioFinal - salario
        print("Seu salário antigo é " + str(salario) + " , seu salario novo é " + str(salarioFinal) + " , com diferença de " + str(salarioDiferença))
