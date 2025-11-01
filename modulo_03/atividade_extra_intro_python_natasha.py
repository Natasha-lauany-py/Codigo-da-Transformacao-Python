# --- Desafio Extra: Saudação com Hora Atual ---

# Importa a biblioteca 'datetime' do Python, que permite trabalhar com datas e horas.
from datetime import datetime

# 1. Pede o nome do usuário (igual à Atividade 3)
nome_usuario = input("Por favor, digite o seu nome: ")

# 2. Obtém a hora atual
# datetime.now() retorna um objeto datetime que contém data e hora atuais.
agora = datetime.now()

# 3. Formata a hora para exibição
# strftime é usado para formatar a data/hora em uma string.
# %H: hora (24h) | %M: minuto | %S: segundo
hora_formatada = agora.strftime("%H:%M:%S")

# 4. Cria a mensagem de saudação completa
# Usamos uma f-string para incluir o nome e a hora formatada.
mensagem_completa = f"Olá, {nome_usuario}! A hora atual é {hora_formatada}. Seja muito bem-vindo(a)."

# 5. Exibe a mensagem
print(mensagem_completa)

# Exemplo de saída no console (se o usuário digitar "João"):
# Por favor, digite o seu nome: João
# Olá, João! A hora atual é 10:45:30. Seja muito bem-vindo(a).# --- Desafio Extra: Saudação com Hora Atual ---

# Importa a biblioteca 'datetime' do Python, que permite trabalhar com datas e horas.
from datetime import datetime

# 1. Pede o nome do usuário (igual à Atividade 3)
nome_usuario = input("Por favor, digite o seu nome: ")

# 2. Obtém a hora atual
# datetime.now() retorna um objeto datetime que contém data e hora atuais.
agora = datetime.now()

# 3. Formata a hora para exibição
# strftime é usado para formatar a data/hora em uma string.
# %H: hora (24h) | %M: minuto | %S: segundo
hora_formatada = agora.strftime("%H:%M:%S")

# 4. Cria a mensagem de saudação completa
# Usamos uma f-string para incluir o nome e a hora formatada.
mensagem_completa = f"Olá, {nome_usuario}! A hora atual é {hora_formatada}. Seja muito bem-vindo(a)."

# 5. Exibe a mensagem
print(mensagem_completa)

# Exemplo de saída no console (se o usuário digitar "João"):
# Por favor, digite o seu nome: João
# Olá, João! A hora atual é 10:45:30. Seja muito bem-vindo(a).