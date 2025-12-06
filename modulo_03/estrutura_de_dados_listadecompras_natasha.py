lista_compras = []

while True:
    print("\n--- Gerenciador de Lista de Compras ---")
    print(f"Itens na lista: {lista_compras}")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Sair")
    print("---------------------------------------")

    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    if opcao == '1':
        item = input("Digite o nome do item a adicionar: ")
        lista_compras.append(item)
        print(f"'{item}' adicionado à lista.")
    elif opcao == '2':
        item = input("Digite o nome do item a remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"'{item}' removido da lista.")
        else:
            print(f"'{item}' não encontrado na lista.")
    elif opcao == '3':
        print("Saindo do programa. Lista final:")
        break
    else:
        print("Opção inválida. Tente novamente.")

