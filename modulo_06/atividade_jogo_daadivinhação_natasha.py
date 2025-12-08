# Usando a biblioteca Faker

from faker import Faker # type: ignore

# Inicializa o Faker, definindo o idioma para Português do Brasil (pt_BR)
fake = Faker('pt_BR') 

def gerar_dados_clientes(quantidade):
    """Gera uma lista de dicionários com dados de clientes fictícios."""
    clientes = []
    print(f"Gerando {quantidade} clientes fictícios...")
    for i in range(1, quantidade + 1):
        cliente = {
            "ID": i,
            "Nome": fake.name(),
            "CPF": fake.cpf(), # CPF é um dado específico do pt_BR
            "Endereço": fake.address(),
            "Email": fake.email(),
            "Data_Nascimento": fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%d/%m/%Y')
        }
        clientes.append(cliente)
    return clientes

# --- Execução da Atividade 2 ---
NUMERO_DE_CLIENTES = 3

dados_gerados = gerar_dados_clientes(NUMERO_DE_CLIENTES)

print("\n--- Dados Fictícios Gerados com Faker ---")
for cliente in dados_gerados:
    print("-" * 30)
    print(f"Nome: {cliente['Nome']}")
    print(f"Email: {cliente['Email']}")
    print(f"CPF: {cliente['CPF']}")
    print(f"Nasc: {cliente['Data_Nascimento']}")