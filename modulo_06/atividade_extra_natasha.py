# dados/processamento.py
def filtrar_dados(dados, condicao):
    """Simula a filtragem de dados."""
    print(f"Processando: Filtro '{condicao}' aplicado em {len(dados)} itens.")
    return [item for item in dados if condicao in item]

def somar_valores(valores):
    """Simula um cálculo simples."""
    return sum(valores)