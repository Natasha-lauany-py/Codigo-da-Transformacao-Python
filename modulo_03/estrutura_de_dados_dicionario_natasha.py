# Cria um dicionário com as informações do aluno
aluno = {
    'nome': 'Maria',
    'idade': 16,
    'notas': [8.5, 9.0, 7.8, 10.0]
}

# Exibe os dados armazenados
print("Dados do aluno:")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Notas: {aluno['notas']}")

# Exibindo de forma iterativa (opcional)
print("\nDados do aluno (iterativo):")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")

