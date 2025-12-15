import requests

def buscar_clima():
    # Substitua pela sua chave API real
    API_KEY = "SUA_CHAVE_DO_OPENWEATHERMAP_AQUI"
    cidade = input("Digite o nome da cidade: ")
    
    # URL base (Atividade 1)
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"

    try:
        # Fazendo a requisição (Atividade 1)
        requisicao = requests.get(link)
        
        # Verifica se houve erro HTTP (4xx ou 5xx) e levanta exceção se houver (Atividade 3)
        requisicao.raise_for_status()

        # Convertendo para dicionário Python
        dic_requisicao = requisicao.json()

        # Extraindo dados específicos (Atividade 2)
        descricao = dic_requisicao['weather'][0]['description']
        temperatura = dic_requisicao['main']['temp']
        umidade = dic_requisicao['main']['humidity']

        # Exibindo de forma organizada (Atividade 2)
        print(f"\n--- Clima em {cidade.capitalize()} ---")
        print(f"🌡️  Temperatura: {temperatura}ºC")
        print(f"☁️  Condição: {descricao.capitalize()}")
        print(f"💧 Umidade: {umidade}%")

    # Blocos de Tratamento de Erro (Atividade 3)
    except requests.exceptions.HTTPError as err:
        if requisicao.status_code == 404:
            print("❌ Erro: Cidade não encontrada. Verifique a grafia.")
        elif requisicao.status_code == 401:
            print("❌ Erro: Chave de API inválida.")
        else:
            print(f"❌ Erro HTTP ocorrido: {err}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Erro de Conexão: Verifique sua internet.")
        
    except requests.exceptions.Timeout:
        print("❌ Erro: O servidor demorou muito para responder.")
        
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

# Executa a função
if __name__ == "__main__":
    buscar_clima()