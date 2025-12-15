# app.py

# Função simples de soma (para Atividade 1)
def soma(a, b):
    return a + b

# Classe Calculadora (para Atividades 2 e 3)
class Calculadora:
    """Uma classe simples para operações matemáticas."""

    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            # Atividade 3: Lança exceção para divisão por zero
            raise ValueError("Não é possível dividir por zero.")
        return a / b

# Para o Desafio Extra (Flask API)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/somar/<int:num1>/<int:num2>', methods=['GET'])
def api_somar(num1, num2):
    """API que utiliza a função soma."""
    resultado = soma(num1, num2)
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    # A API não será executada aqui para os testes, 
    # mas o código está pronto.
    pass