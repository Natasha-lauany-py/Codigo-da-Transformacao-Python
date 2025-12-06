# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza as operações aritméticas
soma = num1 + num2
diferenca = num1 - num2
multiplicacao = num1 * num2
# Verifica se o segundo número é zero para evitar erro de divisão por zero
if num2 != 0:
    divisao = num1 / num2
    resto = num1 % num2
else:
    divisao = "Não é possível dividir por zero"
    resto = "Não é possível calcular o resto com zero"

# Exibe os resultados
print(f"Soma: {soma}")
print(f"Diferença: {diferenca}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto da divisão (módulo): {resto}")

