# Módulo: utilidades.py

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração do primeiro número pelo segundo."""
    return a - b

def potencia(base, expoente):
    """Calcula a potência de uma base elevada a um expoente."""
    # Usando o operador de potência ** em Python
    return base ** expoente

def raiz_quadrada(numero):
    """Calcula a raiz quadrada de um número (usando math.sqrt internamente)."""
    # Exemplo: podemos importar bibliotecas dentro do módulo se necessário
    import math
    if numero < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return math.sqrt(numero)

print("Módulo 'utilidades' carregado.")