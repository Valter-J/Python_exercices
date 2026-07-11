"""
Mercearia - Sistema de Controle de Estoque
------------------------------------------------------
Complete as funções abaixo seguindo as instruções do enunciado.
Não é necessário mudar a estrutura dos dados (a lista `estoque`),
só usá-la.
"""

# Cada produto é: [nome, preco, quantidade]


from asyncio.windows_events import NULL


estoque = [
    ["Arroz 5kg", 28.90, 12],
    ["Feijão 1kg", 8.50, 30],
    ["Óleo de Soja 900ml", 7.20, 4],
    ["Açúcar 5kg", 22.00, 0],
    ["Café 500g", 15.90, 8],
]


def listar_produtos(estoque):
    """Mostra todos os produtos do estoque.
    Se a quantidade for 0, mostrar 'ESGOTADO' no lugar do número.
    """
    # TODO: percorra a lista `estoque` com um for e imprima cada produto

    for p in estoque:
        if ( p[2] > 0 ):
            print("Nome: " + p[0] + " Valor: " + str(p[1]) + " Quantidade: " + str(p[2]))
        else:
            print("Nome: " + str(p[0]) + " Está esgotado")
    
    return True
    

def cadastrar_produto(estoque):
    """Pergunta nome, preço e quantidade e adiciona um novo produto.
    Não deve permitir nomes duplicados.
    """
    # TODO:
    # 1. peça o nome ao usuário
    # 2. verifique se já existe um produto com esse nome no estoque
    # (percorra o estoque comparando os nomes)
    # 3. se já existir, avise e não cadastre
    # 4. se não existir, peça preço e quantidade e adicione à lista

    nome = input("Digite o nome do produto que deseja cadastrar").lower()

    if (buscar_produto(estoque, nome) == NULL):
        addEstoque = []
        addEstoque.append(nome)

        valor = float(input("Digite o valor do produto: "))
        addEstoque.append(valor)

        qtd = int(input("Digite a quantidade do produto: "))
        addEstoque.append(qtd)

        estoque.append(addEstoque)

        print("Produto cadastrado com sucesso")
        
        return True
    else:
        print("Produto ja cadastrado")
        return False


def buscar_produto(estoque, nomeProduto):
    """Pergunta um texto e mostra todos os produtos cujo nome contenha
    esse texto (sem diferenciar maiúsculas/minúsculas).
    """
    # TODO: use .lower() no texto digitado e no nome do produto
    # para comparar sem se importar com maiúsculas/minúsculas    
    for p2 in estoque:
        if (nomeProduto in p2[0].lower()):
            return p2
    
    return NULL
    

def valor_total_estoque(estoque):
    """Calcula e mostra a soma de preco * quantidade de todos os produtos."""
    # TODO: use uma variável acumuladora, comece em 0

    qtdTotal = 0

    for i in estoque:
        qtdTotal += i[1]
        print("Valor total: ")
    return qtdTotal
        

    


def produtos_estoque_baixo(estoque):
    """Pergunta um limite e lista os produtos com quantidade <= limite."""
    # TODO
    
    

    pass


def registrar_venda(estoque):
    """Pergunta produto e quantidade vendida, valida e atualiza o estoque."""
    # TODO:
    # 1. peça o nome do produto
    # 2. procure o produto no estoque
    # 3. se não encontrar, avise
    # 4. se encontrar, peça a quantidade vendida
    # 5. se a quantidade vendida for maior que a disponível, avise e não venda
    # 6. caso contrário, subtraia do estoque e mostre o valor da venda
    pass


def mostrar_menu():
    print("\n=== Mercearia ===")
    print("1 - Listar todos os produtos")
    print("2 - Cadastrar novo produto")
    print("3 - Buscar produto pelo nome")
    print("4 - Ver valor total do estoque")
    print("5 - Ver produtos com estoque baixo")
    print("6 - Registrar uma venda")
    print("0 - Sair")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_produtos(estoque)
        elif opcao == "2":
            cadastrar_produto(estoque)
        elif opcao == "3":
            nomeProduto = input("Digite o nome do produto a ser buscado: ")
            prod = buscar_produto(estoque, nomeProduto)
            if (prod != NULL):
                print(prod)
        elif opcao == "4":
            valor_total_estoque(estoque)
        elif opcao == "5":
            produtos_estoque_baixo(estoque)
        elif opcao == "6":
            registrar_venda(estoque)
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
