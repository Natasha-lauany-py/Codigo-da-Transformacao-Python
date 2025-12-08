# Exceção personalizada para falha de login
class CredenciaisInvalidasError(Exception):
    """Exceção levantada quando o usuário e/ou senha estão incorretos."""
    pass

def sistema_login(max_tentativas=3):
    """Simula um sistema de login com limite de tentativas."""
    
    # Credenciais esperadas
    USUARIO_CORRETO = "admin"
    SENHA_CORRETA = "123456"
    
    tentativas = 0
    print("\n--- Desafio Extra: Sistema de Login ---")

    while tentativas < max_tentativas:
        try:
            usuario = input("Usuário: ")
            senha = input("Senha: ")
            
            # 1. Verifica as credenciais
            if usuario != USUARIO_CORRETO or senha != SENHA_CORRETA:
                # 2. Levanta a exceção se estiver incorreto
                raise CredenciaisInvalidasError("Usuário ou senha incorretos.")
            
            # Se as credenciais estiverem corretas (não houve exceção)
            print("\n🎉 Login realizado com sucesso! Bem-vindo(a) ao sistema.")
            return # Sai da função após o sucesso

        except CredenciaisInvalidasError as e:
            tentativas += 1
            restantes = max_tentativas - tentativas
            
            print(f"\n❌ ERRO: {e}")
            
            # 3. Informa as tentativas restantes
            if restantes > 0:
                print(f"Você tem mais {restantes} tentativa(s).")
            
        except Exception as e:
            # Captura qualquer outro erro inesperado
            print(f"\n❌ Erro Inesperado: {e}")
            tentativas += 1

    # 4. Bloqueia após esgotar as tentativas
    print("\n🔒 Todas as tentativas foram esgotadas. Sistema bloqueado.")

# --- Execução do Desafio Extra ---
sistema_login()