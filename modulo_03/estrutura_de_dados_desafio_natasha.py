agenda_contatos = {}

def adicionar_contato(nome, telefone):
    agenda_contatos[nome] = telefone
    print(f"Contato '{nome}' adicionado com sucesso.")

def remover_contato(nome):
    if nome in agenda_contatos:
        del agenda_contatos[nome]
        print(f"Contato '{nome}' removido com sucesso.")
    else:
        print(f"Contato '{nome}' não encontrado na agenda.")

def buscar_contato(nome):
    if nome in agenda_contatos:
        print(f"Telefone de '{nome}': {agenda_contatos[nome]}")
    else:
        print(f"Contato '{nome}' não encontrado na agenda.")

def visualizar_contatos():
    if agenda_contatos:
        print("\n--- Lista de Contatos ---")
        for nome, telefone in agenda_contatos.items():
            print(f"Nome: {nome} | Telefone: {telefone}")
        print("-------------------------")
    else:
        print("A agenda de contatos está vazia.")

# Exemplo de uso:
adicionar_contato("Alice", "11987654321")
adicionar_contato("Bob", "21912345678")
visualizar_contatos()
buscar_contato("Alice")
remover_contato("Bob")
visualizar_contatos()

