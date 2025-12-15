import sqlite3

def conectar():
    return sqlite3.connect('tarefas.db')

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_tarefa(descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Tarefas (descricao) VALUES (?)", (descricao,))
    conn.commit()
    conn.close()
    print("✅ Tarefa adicionada!")

def visualizar_tarefas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    
    print("\n--- LISTA DE TAREFAS ---")
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for t in tarefas:
            print(f"ID: {t[0]} | Descrição: {t[1]}")
    print("------------------------\n")

def excluir_tarefa(id_tarefa):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Tarefas WHERE id = ?", (id_tarefa,))
    if cursor.rowcount > 0:
        print("🗑️ Tarefa excluída!")
    else:
        print("⚠️ ID não encontrado.")
    conn.commit()
    conn.close()

def menu():
    criar_tabela()
    while True:
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Excluir Tarefa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            desc = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(desc)
        elif opcao == '2':
            visualizar_tarefas()
        elif opcao == '3':
            try:
                id_t = int(input("Digite o ID da tarefa para excluir: "))
                excluir_tarefa(id_t)
            except ValueError:
                print("Por favor, digite um número válido.")
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()