import json
import os

# Dados de exemplo: um dicionário de clientes
clientes = {
    "1001": {"nome": "Maria Silva", "email": "maria@exemplo.com"},
    "1002": {"nome": "João Souza", "email": "joao@exemplo.com"},
    "1003": {"nome": "Ana Lima", "email": "ana@exemplo.com"}
}

# 1. Salvar o dicionário em JSON
def salvar_json(nome_arquivo, dados):
    """Salva um dicionário em um arquivo JSON."""
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            # indent=4 é usado para formatar o JSON de forma legível
            json.dump(dados, arquivo, indent=4)
        print(f"✅ Dicionário de clientes salvo com sucesso em '{nome_arquivo}'.")
    except IOError as e:
        print(f"❌ Erro ao salvar o arquivo JSON: {e}")

# 2. Carregar o JSON em um dicionário
def carregar_json(nome_arquivo):
    """Carrega dados de um arquivo JSON para um dicionário Python."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados_carregados = json.load(arquivo)
        return dados_carregados
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return {}
    except json.JSONDecodeError:
        print(f"❌ Erro: O arquivo '{nome_arquivo}' não está em um formato JSON válido.")
        return {}

# --- Execução da Atividade 2 ---
nome_arquivo_json = "clientes.json"

# Salvar
salvar_json(nome_arquivo_json, clientes)

# Carregar e Exibir
print("\n--- Dados de Clientes Carregados do JSON ---")
clientes_carregados = carregar_json(nome_arquivo_json)
if clientes_carregados:
    for id_cliente, dados in clientes_carregados.items():
        print(f"ID: {id_cliente}, Nome: {dados['nome']}, Email: {dados['email']}")
