import sqlite3
from flask import Flask, jsonify, request

# --- 1. Configuração do Flask e Banco de Dados ---

app = Flask(__name__)
DATABASE = 'users.db'

def get_db_connection():
    """Cria e retorna uma conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn

def init_db():
    """Inicializa o banco de dados e cria a tabela 'users' se ela não existir."""
    with app.app_context():
        conn = get_db_connection()
        # Criando a tabela para armazenar os dados dos usuários
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        ''')
        conn.commit()
        conn.close()

# Inicializa o banco de dados ao iniciar o script
init_db()


# --- 1. Rota GET /saudacao ---

@app.route('/saudacao', methods=['GET'])
def saudacao():
    """Configura um servidor Flask básico e implementa uma rota /saudacao."""
    return jsonify({
        'message': 'Olá! Bem-vindo(a) à API Flask para o Módulo 13!'
    }), 200


# --- 2. e 3. Rota POST /cadastrar com persistência SQLite ---

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    """Cria uma rota POST /cadastrar para receber dados de usuário via JSON e persistir no SQLite."""
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        return jsonify({
            'error': 'Dados inválidos. Os campos "name" e "email" são obrigatórios.'
        }), 400

    name = data['name']
    email = data['email']

    try:
        conn = get_db_connection()
        # Inserir os dados na tabela 'users'
        conn.execute(
            'INSERT INTO users (name, email) VALUES (?, ?)',
            (name, email)
        )
        conn.commit()
        conn.close()

        return jsonify({
            'message': 'Usuário cadastrado com sucesso!',
            'user': {'name': name, 'email': email}
        }), 201

    except sqlite3.IntegrityError:
        # Lidar com erros como e-mail duplicado
        return jsonify({
            'error': 'Erro de integridade: O e-mail fornecido já está em uso.'
        }), 409
    except Exception as e:
        # Lidar com outros erros de banco de dados
        return jsonify({
            'error': f'Erro ao cadastrar usuário: {str(e)}'
        }), 500


# --- Rota para listar todos os usuários (Opcional, mas útil para verificar) ---

@app.route('/users', methods=['GET'])
def listar_usuarios():
    """Rota auxiliar para listar todos os usuários cadastrados."""
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()

    # Converte os objetos Row do SQLite para dicionários Python
    users_list = []
    for user in users:
        users_list.append(dict(user))

    return jsonify(users_list), 200


if __name__ == '__main__':
    app.run(debug=True)