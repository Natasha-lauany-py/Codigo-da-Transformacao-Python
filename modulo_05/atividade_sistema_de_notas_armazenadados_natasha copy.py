import csv
import os

NOME_ARQUIVO_CSV = "notas_alunos.csv"
CABECALHO = ["Aluno", "Materia", "Nota"]

# 1. Inicializa o arquivo CSV se ele não existir
def inicializar_csv():
    """Cria o arquivo CSV com o cabeçalho se ele não existir."""
    if not os.path.exists(NOME_ARQUIVO_CSV):
        with open(NOME_ARQUIVO_CSV, 'w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(CABECALHO)
        print(f"Arquivo '{NOME_ARQUIVO_CSV}' inicializado com cabeçalho.")

# 2. Adicionar notas de alunos
def adicionar_nota(aluno, materia, nota):
    """Adiciona uma nova linha de nota ao arquivo CSV (modo 'a' - append)."""
    try:
        # 'a': modo de anexo (adiciona no final), 'newline='': evita linhas em branco
        with open(NOME_ARQUIVO_CSV, 'a', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([aluno, materia, nota])
        print(f"✅ Nota de {aluno} adicionada com sucesso.")
    except IOError as e:
        print(f"❌ Erro ao adicionar nota: {e}")

# 3. Carregar e exibir as informações
def carregar_e_exibir_notas():
    """Lê todas as notas do arquivo CSV e as exibe."""
    notas_carregadas = []
    try:
        with open(NOME_ARQUIVO_CSV, 'r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            
            # Pula o cabeçalho (a primeira linha)
            next(leitor)
            
            for linha in leitor:
                # A linha é uma lista: [Aluno, Materia, Nota]
                notas_carregadas.append(linha)
        
        return notas_carregadas
    
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo '{NOME_ARQUIVO_CSV}' não foi encontrado. Inicializando...")
        inicializar_csv()
        return []
    except IOError as e:
        print(f"❌ Erro ao ler o arquivo CSV: {e}")
        return []

# --- Execução da Atividade 3 ---

# Garante que o arquivo exista
inicializar_csv()

# Adicionar novas notas
adicionar_nota("Carlos", "Matemática", 8.5)
adicionar_nota("Sofia", "Português", 9.2)
adicionar_nota("Carlos", "Física", 7.0)

# Carregar e Exibir
print("\n--- Notas de Alunos Carregadas do CSV ---")
todas_as_notas = carregar_e_exibir_notas()

if todas_as_notas:
    # Imprime o cabeçalho da tabela
    print(f"{CABECALHO[0]:<15} | {CABECALHO[1]:<15} | {CABECALHO[2]:>5}")
    print("-" * 38)
    for nota in todas_as_notas:
        # nota[0]=Aluno, nota[1]=Materia, nota[2]=Nota
        print(f"{nota[0]:<15} | {nota[1]:<15} | {nota[2]:>5}")