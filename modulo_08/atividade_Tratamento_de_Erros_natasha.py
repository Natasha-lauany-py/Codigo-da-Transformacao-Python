def calculadora_divisao():
    """Realiza uma divisão e trata o erro de divisão por zero."""
    print("\n--- Calculadora de Divisão ---")
    
    try:
        # Pede a entrada de dois números
        num1 = float(input("Digite o numerador (número a ser dividido): "))
        num2 = float(input("Digite o denominador (divisor): "))
        
        # Tenta realizar a operação de divisão
        resultado = num1 / num2
        
    # Captura a exceção específica de divisão por zero
    except ZeroDivisionError:
        print("\n❌ Erro: Divisão por zero não é permitida na matemática.")
        print("Tente novamente com um divisor diferente de zero.")
        return # Sai da função após o erro
        
    # Captura outros erros que possam ocorrer na entrada (ex: digitar texto)
    except ValueError:
        print("\n❌ Erro: Entrada inválida. Por favor, digite apenas números.")
        return
        
    # Bloco 'else' é executado SOMENTE se o bloco 'try' for bem-sucedido
    else:
        print(f"\n✅ Resultado da divisão de {num1} por {num2} é: {resultado}")
        
    # Bloco 'finally' é executado sempre, independentemente de erro
    finally:
        print("Operação de cálculo finalizada.")

# --- Testando a Atividade 1 ---
calculadora_divisao()