conjunto_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = []
numeros_impares = []

# Percorre o conjunto de números
for numero in conjunto_numeros:
    # Verifica se o resto da divisão por 2 é zero
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

# Exibe as listas separadamente
print(f"Conjunto original: {conjunto_numeros}")
print(f"Números pares: {numeros_pares}")
print(f"Números ímpares: {numeros_impares}")

