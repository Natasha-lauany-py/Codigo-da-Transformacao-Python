# 1. Cria a exceção personalizada, herdando da classe Exception
class SaldoInsuficienteError(Exception):
    """Exceção levantada quando há saldo insuficiente para a operação."""
    # O construtor personalizado ajuda a passar uma mensagem útil
    def __init__(self, saldo_atual, valor_saque):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        mensagem = (f"Saldo insuficiente para saque de R$ {valor_saque:.2f}. "
                    f"Saldo atual: R$ {saldo_atual:.2f}")
        # Chama o construtor da classe pai (Exception)
        super().__init__(mensagem)

class ContaBancaria:
    """Simula uma conta bancária simples."""
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial
        print(f"Conta de {titular} criada com saldo inicial de R$ {saldo_inicial:.2f}.")

    def sacar(self, valor):
        """Tenta realizar um saque, levantando uma exceção se o saldo for insuficiente."""
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
            
        if self.saldo < valor:
            # Levanta a exceção personalizada
            raise SaldoInsuficienteError(self.saldo, valor)
        
        self.saldo -= valor
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso.")
        print(f"Novo saldo: R$ {self.saldo:.2f}")

# --- Testando a Atividade 2 ---
print("\n--- Teste 2: Exceção Personalizada ---")
minha_conta = ContaBancaria("João Silva", 500.00)

try:
    # 1. Saque bem-sucedido
    minha_conta.sacar(150.00) 
    
    # 2. Saque que deve falhar e levantar a exceção
    minha_conta.sacar(400.00) 

# Captura a exceção personalizada, tratando-a de forma específica
except SaldoInsuficienteError as e:
    print(f"\n❌ ERRO NA OPERAÇÃO BANCÁRIA: {e}") 
    print(f"Recomendação: O cliente deve depositar pelo menos R$ {e.valor_saque - e.saldo_atual:.2f}.")
except ValueError as e:
    print(f"\n❌ ERRO NA VALIDAÇÃO: {e}")