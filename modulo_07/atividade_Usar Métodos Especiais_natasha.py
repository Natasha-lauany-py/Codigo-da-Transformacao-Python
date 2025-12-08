class CarroFormatado:
    """
    Classe Carro revisada para incluir __str__.
    """
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    # 1. Método especial __str__ para representação em string
    def __str__(self):
        """
        Retorna uma representação amigável do objeto CarroFormatado.
        É usado automaticamente pela função print().
        """
        return f"Carro: {self.marca} {self.modelo} ({self.ano})"

# --- Testando o Método Especial __str__ ---
print("\n--- Teste 3: Métodos Especiais (__str__) ---")
carro_novo = CarroFormatado("Toyota", "Corolla", 2024)

# O Python chama automaticamente carro_novo.__str__()
print("Resultado do print(carro_novo):")
print(carro_novo) 

# Convertendo explicitamente para string
representacao_str = str(carro_novo)
print(f"Resultado de str(carro_novo): {representacao_str}")
