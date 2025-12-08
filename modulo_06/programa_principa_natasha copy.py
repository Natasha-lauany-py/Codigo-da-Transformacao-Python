# Programa Principal: programa_principal.py

# Opção 1: Importar o módulo inteiro
import utilidades as u # type: ignore

# Opção 2: Importar funções específicas (não recomendado se já usou a Opção 1)
# from utilidades import somar, potencia 

print("\n--- Testando as Funções do Módulo ---")

# Usando as funções importadas
resultado_soma = u.somar(15, 7)
print(f"1. Soma de 15 + 7: {resultado_soma}") # Saída: 22

resultado_subtracao = u.subtrair(30, 12)
print(f"2. Subtração de 30 - 12: {resultado_subtracao}") # Saída: 18

resultado_potencia = u.potencia(2, 5)
print(f"3. Potência de 2 elevado a 5: {resultado_potencia}") # Saída: 32

try:
    resultado_raiz = u.raiz_quadrada(81)
    print(f"4. Raiz quadrada de 81: {resultado_raiz}") # Saída: 9.0
except ValueError as e:
    print(f"Erro: {e}")