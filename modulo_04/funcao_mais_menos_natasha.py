def maior_menor(lista_de_numeros):
    if not lista_de_numeros:
        return None, None
    maior = max(lista_de_numeros)
    menor = min(lista_de_numeros)
    return maior, menor

# Exemplo de uso:
numeros = [10, 50, 30, 70, 20]
maior, menor = maior_menor(numeros)
print(f"Lista: {numeros}")
print(f"Maior valor: {maior}, Menor valor: {menor}")

numeros2 = [3, 1, 4, 1, 5, 9, 2, 6]
maior2, menor2 = maior_menor(numeros2)
print(f"Lista: {numeros2}")
print(f"Maior valor: {maior2}, Menor valor: {menor2}")
