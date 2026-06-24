import math

opcao = 0

while(opcao != 5):

    print("CALCULE QUANTAS CAIXAS A DONA V Precisa comprar conforme todos os seus remédios prescritos")
    print("Digite 1 para cacular a caixa do Prixicliato de Citamina")
    print("Digite 2 para cacular a caixa do Zitaropan:")
    print("Digite 3 para cacular a caixa Madozol")
    print("Digite 4 para cacular a caixa do Tilazinan")
    print("Digite 5 para Sair")
    opcao = int(input())

    match opcao:
        case 1:

            medioPrixicita = int(input("Digite quantos comprimidos de Prixicliato de Citamina Dona V tem: "))
            valorTotalMes = 30 * int(input("Digite quantos quantas vezes pode dia Dona V toma o remédio: "))
           

            if (medioPrixicita <= valorTotalMes):
                
                faltanteMedioPrixicita = valorTotalMes - medioPrixicita
                caixaTotal = math.ceil((faltanteMedioPrixicita / 30))

                print("Falta " + str(caixaTotal) + " caixas de compridos de Prixicliato de Citamina para o próximo mês")
            else:
                # TODO: Tem como melhorar aqui
                print("Dona V tem os comprimitos necessario para o mês")


        case 2:

            medioZitaropan = int(input("Digite quantos comprimidos de Zitaropan Dona V tem: "))
            valorTotalMes = 30 * int(input("Digite quantos quantas vezes pode dia Dona V toma o remédio: "))
           

            if ( medioZitaropan <= valorTotalMes):
                
                faltanteMedioZitaropan = valorTotalMes - medioZitaropan
                caixaTotal = math.ceil((faltanteMedioZitaropan / 60))

                print("Falta " + str(caixaTotal) + " caixas de compridos de Zitaropan para o próximo mês")
            else:
                # TODO: Tem como melhorar aqui
                print("Dona V tem os comprimitos necessario para o mês")

        case 3:

            medioMadozol = int(input("Digite quantos comprimidos de Madozol Dona V tem: "))
            valorTotalMes = 30 * int(input("Digite quantos quantas vezes pode dia Dona V toma o remédio: "))
           

            if ( medioMadozol <= valorTotalMes):
                
                faltanteMedioMadozol = valorTotalMes - medioMadozol
                caixaTotal = math.ceil((faltanteMedioMadozol / 15))

                print("Falta " + str(caixaTotal) + " caixas de compridos de Madozol para o próximo mês")
            else:
                # TODO: Tem como melhorar aqui
                print("Dona V tem os comprimitos necessario para o mês")

        case 4:

            medioTilazinan = int(input("Digite quantos comprimidos de Tilazinan Dona V tem: "))
            valorTotalMes = 30 * int(input("Digite quantos quantas vezes pode dia Dona V toma o remédio: "))
           

            if ( medioTilazinan<= valorTotalMes):
                
                faltanteMedioTilazinan = valorTotalMes - medioTilazinan
                caixaTotal = math.ceil((faltanteMedioTilazinan / 30))

                print("Falta " + str(caixaTotal) + " caixas de compridos de Tilazinan para o próximo mês")
            else:
                # TODO: Tem como melhorar aqui
                print("Dona V tem os comprimitos necessario para o mês")
                   