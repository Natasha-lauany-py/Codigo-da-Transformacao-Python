import requests

def buscar_filme():
    # Substitua pela sua chave API do TMDB
    API_KEY = "SUA_CHAVE_DO_TMDB_AQUI"
    filme_nome = input("Digite o nome do filme que deseja pesquisar: ")
    
    # Endpoint de busca (Search Movie)
    url = "https://api.themoviedb.org/3/search/movie"
    
    params = {
        "api_key": API_KEY,
        "query": filme_nome,
        "language": "pt-BR"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        dados = response.json()
        
        # Verifica se encontrou algum resultado
        if dados['results']:
            # Pega o primeiro resultado da busca (o mais relevante)
            filme = dados['results'][0]
            
            titulo = filme['title']
            sinopse = filme['overview']
            lancamento = filme['release_date']
            nota = filme['vote_average']

            print(f"\n🎬 Título: {titulo}")
            print(f"📅 Lançamento: {lancamento}")
            print(f"⭐ Nota: {nota}")
            print(f"📝 Sinopse: {sinopse if sinopse else 'Sem sinopse disponível.'}")
        else:
            print("❌ Nenhum filme encontrado com esse nome.")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao conectar com a API do TMDB: {e}")

# Executa a função do desafio
if __name__ == "__main__":
    print("\n--- Desafio Extra: Buscador de Filmes ---")
    buscar_filme()