import shutil
import os

# --- Configurações do Backup ---
PASTA_ORIGEM = "arquivos_originais"
PASTA_DESTINO = "backup_diario"

# 1. Prepara as pastas de origem e cria arquivos de exemplo
def preparar_ambiente():
    """Cria pastas e arquivos para simular um cenário de backup."""
    # Cria a pasta de origem se não existir
    if not os.path.exists(PASTA_ORIGEM):
        os.makedirs(PASTA_ORIGEM)
        print(f"Pasta de origem '{PASTA_ORIGEM}' criada.")
    
    # Cria a pasta de destino (o shutil.copytree a criará, mas é bom ter o controle)
    if not os.path.exists(PASTA_DESTINO):
        os.makedirs(PASTA_DESTINO)
    
    # Cria alguns arquivos de exemplo na pasta de origem
    arquivos_exemplo = ["documento_a.txt", "imagem_b.jpg", "planilha_c.xlsx"]
    for nome_arquivo in arquivos_exemplo:
        caminho_completo = os.path.join(PASTA_ORIGEM, nome_arquivo)
        if not os.path.exists(caminho_completo):
            with open(caminho_completo, 'w') as f:
                f.write(f"Conteúdo de {nome_arquivo}")
            print(f"Arquivo '{nome_arquivo}' criado em '{PASTA_ORIGEM}'.")

# 2. Realiza a cópia de backup
def fazer_backup(origem, destino):
    """Copia todo o conteúdo de uma pasta para outra."""
    try:
        # Remove a pasta de destino se ela já existir para simular um backup 'limpo'
        # Isso é crucial para copytree se a pasta de destino já tiver conteúdo
        if os.path.exists(destino):
            shutil.rmtree(destino)
        
        # Copia todo o diretório de origem para o diretório de destino
        shutil.copytree(origem, destino)
        print(f"\n🚀 SUCESSO! Backup completo de '{origem}' para '{destino}' realizado.")
    
    except shutil.Error as e:
        print(f"❌ Erro de shutil: {e}")
    except IOError as e:
        print(f"❌ Erro de I/O: {e}")

# --- Execução do Desafio Extra ---
preparar_ambiente()
fazer_backup(PASTA_ORIGEM, PASTA_DESTINO)
import os

