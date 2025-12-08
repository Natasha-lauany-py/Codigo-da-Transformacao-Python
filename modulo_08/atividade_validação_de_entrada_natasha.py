def obter_idade_valida():
    """Pede a idade do usuário e garante que seja um número inteiro positivo."""
    
    while True:
        try:
            # Pede a entrada do usuário
            idade_str = input("Digite sua idade: ")
            idade = int(idade_str)
            
            # Validação 1: Garantir que a idade seja positiva
            if idade <= 0:
                print("⚠️ A idade deve ser um número inteiro positivo.")
                # Continua o loop para pedir novamente
                continue 
            
            # Se chegou até aqui, a entrada é um inteiro positivo e válida
            return idade
        
        # Captura o erro se a conversão para inteiro falhar (ex: digitou "vinte")
        except ValueError:
            print("❌ Erro: Por favor, digite um número inteiro válido para a idade.")

# --- Testando a Atividade 3 ---
print("\n--- Teste 3: Validação de Entrada de Usuário ---")
idade_usuario = obter_idade_valida()
print(f"\n✅ Idade válida inserida: {idade_usuario} anos. Processando...")