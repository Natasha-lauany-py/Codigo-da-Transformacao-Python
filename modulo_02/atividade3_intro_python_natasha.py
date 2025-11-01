# --- Atividade 3: Saudação Personalizada ---

# A função 'input()' solicita ao usuário que digite algo no console
# e armazena o que foi digitado na variável 'nome_usuario'.
nome_usuario = input("Por favor, digite o seu nome: ")

# A variável 'mensagem' armazena a saudação.
# Usamos a formatação de string (f-string) para incorporar o valor
# da variável 'nome_usuario' dentro da string de maneira fácil e legível.
mensagem = f"Olá, {nome_usuario}! Seja muito bem-vindo(a) ao mundo Python."

# A função 'print()' exibe a mensagem personalizada na tela.
print(mensagem)

# Exemplo de saída no console (se o usuário digitar "Maria"):
# Por favor, digite o seu nome: Maria
# Olá, Maria! Seja muito bem-vindo(a) ao mundo Python. 