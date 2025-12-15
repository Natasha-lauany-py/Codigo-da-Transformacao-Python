import sqlite3

def main():
    # 1. Configuração do banco de dados e criação da tabela
    # O arquivo 'meu_banco.db' será criado automaticamente
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    # Criação da tabela Clientes (se não existir)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conexao.commit()
    print("--- Tabela criada com sucesso! ---")

    # 2. Operações CRUD

    # --- CREATE (Inserir) ---
    lista_clientes = [
        ('Ana Paula', 'ana@email.com'),
        ('Bruno Silva', 'bruno@email.com'),
        ('Carlos Souza', 'carlos@email.com'),
        ('Amanda Dias', 'amanda@email.com')
    ]
    cursor.executemany("INSERT INTO Clientes (nome, email) VALUES (?, ?)", lista_clientes)
    conexao.commit()
    print(f"\n{len(lista_clientes)} clientes inseridos.")

    # --- READ (Consultar Todos) ---
    print("\n--- Todos os Clientes ---")
    cursor.execute("SELECT * FROM Clientes")
    for linha in cursor.fetchall():
        print(linha)

    # --- UPDATE (Atualizar) ---
    # Vamos mudar o email do Bruno
    cursor.execute("UPDATE Clientes SET email = ? WHERE nome = ?", ('bruno_novo@email.com', 'Bruno Silva'))
    conexao.commit()
    print("\n--- Cliente Bruno atualizado ---")

    # --- DELETE (Deletar) ---
    # Vamos deletar o Carlos
    cursor.execute("DELETE FROM Clientes WHERE nome = ?", ('Carlos Souza',))
    conexao.commit()
    print("\n--- Cliente Carlos deletado ---")

    # 3. Consultas com Filtros (Clientes que começam com "A")
    print("\n--- Clientes que começam com a letra 'A' ---")
    cursor.execute("SELECT * FROM Clientes WHERE nome LIKE 'A%'")
    clientes_a = cursor.fetchall()
    
    for cliente in clientes_a:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")

    # Fechar conexão
    conexao.close()

if __name__ == "__main__":
    main()