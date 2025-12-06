while True:
    print("\n--- Menu de Operações ---")
    print("1. Soma")
    print("2. Subtração")
    print("3. Sair")
    print("-------------------------")

    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    if opcao == '3':
        print("Saindo do programa. Até logo!")
        break # Sai do loop while

    elif opcao in ('1', '2'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            resultado = num1 + num2
            print(f"Resultado da Soma: {resultado}")
        elif opcao == '2':
            resultado = num1 - num2
            print(f"Resultado da Subtração: {resultado}")
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

