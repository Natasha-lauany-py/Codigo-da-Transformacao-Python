# ====================================================================
# ATIVIDADE 2: Teste comandos simples no interpretador Python
# Esta seção demonstra comandos básicos como print() e type()
# ====================================================================

print("--- Demonstração da Atividade 2 ---")

# 1. Comando 'print()': Exibe mensagens no console.
print("Este é o primeiro passo: exibir uma mensagem na tela.")

# 2. Operações matemáticas dentro do print.
print("O resultado de 5 vezes 8 é:", 5 * 8)

# 3. Comando 'type()': Identifica o tipo de dado de uma variável ou valor.

# Variável 'inteiro' (int)
numero_inteiro = 42
print(f"O tipo de dado de {numero_inteiro} é:", type(numero_inteiro)) 

# Variável 'texto' (str)
texto = "Python é legal"
print(f"O tipo de dado de '{texto}' é:", type(texto))

# Variável 'decimal' (float)
numero_decimal = 3.14
print(f"O tipo de dado de {numero_decimal} é:", type(numero_decimal))

print("-" * 40) # Linha divisória

# ====================================================================
# ATIVIDADE 3: Crie um programa que pede o nome do usuário 
# e exibe uma mensagem personalizada.
# ====================================================================

print("--- Demonstração da Atividade 3 ---")

# A função 'input()' solicita ao usuário que digite seu nome e armazena na variável.
nome_usuario = input("Por favor, digite o seu nome para a saudação: ")

# Cria a mensagem de saudação usando uma f-string para incorporar a variável 'nome_usuario'.
mensagem_saudacao = f"Olá, {nome_usuario}! Que bom ter você aqui."

# Exibe a mensagem personalizada.
print(mensagem_saudacao)

print("-" * 40)

# ====================================================================
# DESAFIO EXTRA: Exibir a hora atual junto com a saudação.
# Requer a biblioteca 'datetime' para manipulação de data e hora.
# ====================================================================

print("--- Demonstração do Desafio Extra ---")

# Importa a classe 'datetime' do módulo 'datetime'.
from datetime import datetime

# Se o nome já foi solicitado (como na Atividade 3), podemos reutilizá-lo,
# mas pediremos novamente para que a demonstração do Desafio Extra seja independente:
nome_desafio = input("Digite seu nome novamente para o Desafio Extra: ")

# 1. Obtém a data e hora atual do sistema.
agora = datetime.now()

# 2. Formata apenas a hora, minuto e segundo (HH:MM:SS) em uma string.
hora_formatada = agora.strftime("%H:%M:%S")

# 3. Cria a mensagem de boas-vindas completa, incluindo a hora atual.
mensagem_desafio = f"Seja bem-vindo(a), {nome_desafio}! A hora atual é {hora_formatada}. Desafio Extra concluído!"

# 4. Exibe a mensagem final.
print(mensagem_desafio)

print("-" * 40)