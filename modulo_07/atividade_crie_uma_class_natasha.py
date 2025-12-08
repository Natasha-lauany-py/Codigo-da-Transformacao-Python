class Carro:
    """Representa um veículo com marca e modelo."""

    # 1. Método construtor para inicializar os atributos (personalizado)
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        print(f"Objeto Carro '{modelo}' criado.")

    # 2. Método para exibir as informações
    def exibir_info(self):
        """Exibe a marca e o modelo do carro."""
        print(f"  Marca: {self.marca}")
        print(f"  Modelo: {self.modelo}")

# --- Testando a Classe Base ---
print("--- Teste 1: Classe Carro ---")
carro_gasolina = Carro("Ford", "Fusion")
carro_gasolina.exibir_info()
