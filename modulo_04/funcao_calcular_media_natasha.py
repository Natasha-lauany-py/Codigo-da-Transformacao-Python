def calcular_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 7:
        print(f"Média: {media:.2f}. Resultado: Aprovado")
    else:
        print(f"Média: {media:.2f}. Resultado: Reprovado")

# Exemplo de uso:
calcular_media(7, 8, 9, 6)
calcular_media(5, 6, 4, 5)
