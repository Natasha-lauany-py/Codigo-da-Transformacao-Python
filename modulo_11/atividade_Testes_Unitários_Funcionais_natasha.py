# testes.py
import unittest
import pytest
from app import soma, Calculadora, app

# --- Solução para Atividades 1, 2 e 3 (Módulo unittest) ---

class TestApp(unittest.TestCase):
    """
    Testes para as funções e classes da aplicação.
    """

    # Atividade 1: Teste para a função de soma simples
    def test_soma_simples(self):
        self.assertEqual(soma(5, 3), 8)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)

    # Atividade 2: Testes para a classe Calculadora
    def test_calculadora_somar(self):
        calc = Calculadora()
        self.assertEqual(calc.somar(10, 5), 15)
        self.assertEqual(calc.somar(-10, 5), -5)

    def test_calculadora_dividir(self):
        calc = Calculadora()
        self.assertEqual(calc.dividir(10, 2), 5)
        self.assertAlmostEqual(calc.dividir(1, 3), 0.3333333333333333) # Números com ponto flutuante

    # Atividade 3: Validação de entradas inválidas (Exceções)
    def test_divisao_por_zero_lanca_excecao(self):
        calc = Calculadora()
        # O self.assertRaises garante que o código lança a exceção esperada
        with self.assertRaises(ValueError) as context:
            calc.dividir(10, 0)
        
        # Opcional: verifica se a mensagem da exceção está correta
        self.assertTrue('Não é possível dividir por zero.' in str(context.exception))


# --- Solução para Desafio Extra (pytest e Flask API) ---

# O pytest automaticamente encontra funções que começam com 'test_'

@pytest.fixture
def client():
    """Fixture que configura o cliente de teste Flask."""
    app.config['TESTING'] = True
    # 'client()' permite simular requisições HTTP para a API
    with app.test_client() as client:
        yield client

def test_api_somar_sucesso(client):
    """Testa o endpoint da API com valores válidos."""
    # Simula uma requisição GET para /somar/10/5
    response = client.get('/somar/10/5') 
    
    assert response.status_code == 200
    # response.get_json() é o corpo da resposta JSON
    assert response.get_json() == {"resultado": 15}

def test_api_somar_negativos(client):
    """Testa o endpoint da API com números negativos."""
    response = client.get('/somar/-10/3') 
    
    assert response.status_code == 200
    assert response.get_json() == {"resultado": -7}


# Bloco principal para execução dos testes unittest (Atividades 1, 2 e 3)
if __name__ == '__main__':
    # Executa a suíte de testes do unittest
    print("--- Executando testes unittest (Atividades 1, 2 e 3) ---")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    print("---------------------------------------------------------")
    
    # Para rodar os testes do pytest (Desafio Extra), use o terminal:
    # pytest testes.py