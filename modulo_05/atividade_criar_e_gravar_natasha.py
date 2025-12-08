
import os

# 1. Cria o arquivo e grava as informações (modo 'w' - write)
def gravar_arquivo_txt(nome_arquivo, dados):
    """Grava o conteúdo no arquivo, sobrescrevendo o que existe."""
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(dados)
        print(f"✅ Dados gravados com sucesso em '{nome_arquivo}'.")
    except IOError as e:
        print(f"❌ Erro ao gravar o arquivo: {e}")

# 2. Lê as informações a partir do arquivo (modo 'r' - read)
def ler_arquivo_txt(nome_arquivo):
    """Lê e retorna o conteúdo completo do arquivo."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except IOError as e:
        print(f"❌ Erro ao ler o arquivo: {e}")
        return None

# --- Execução da Atividade 1 ---
nome_arquivo_txt = "informacoes.txt"
dados_para_gravar = "Linha 1: Este é um teste de gravação.\nLinha 2: O Python facilita a manipulação de arquivos!"

# Gravar
gravar_arquivo_txt(nome_arquivo_txt, dados_para_gravar)

# Ler e Exibir
print("\n--- Conteúdo do Arquivo .txt ---")
conteudo_lido = ler_arquivo_txt(nome_arquivo_txt)
if conteudo_lido:
    print(conteudo_lido)