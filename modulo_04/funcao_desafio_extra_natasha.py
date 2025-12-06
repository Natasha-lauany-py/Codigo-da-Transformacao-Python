def validar_login(usuario, senha):
    usuarios_db = {
        "admin": "senha123",
        "user1": "pass456",
        "joao": "12345"
    }

    if usuario in usuarios_db and usuarios_db[usuario] == senha:
        print(f"Login bem-sucedido. Bem-vindo(a), {usuario}!")
        return True
    else:
        print("Usuário ou senha inválidos.")
        return False

# Exemplo de uso:
validar_login("admin", "senha123")
validar_login("joao", "senhaerrada")
validar_login("usuarioinexistente", "qualquercoisa")
