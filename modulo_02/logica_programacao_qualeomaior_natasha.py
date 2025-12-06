# Solicita dois números inteiros ao usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Compara os números e exibe o resultado
if num1 > num2:
    print(f"O primeiro número ({num1}) é maior que o segundo número ({num2}).")
elif num2 > num1:
    print(f"O segundo número ({num2}) é maior que o primeiro número ({num1}).")
else:
    print(f"Ambos os números ({num1} e {num2}) são iguais.")

