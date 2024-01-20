import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
# Pegar as informações = get
response = requests.get(url=url)
print(response)

if response.status_code == 200: # Se conseguir captar os dados (status == 200) continua;
    # Pega os dados do JSON que foi respondido
    dados_json = response.json()
    
    # Cria um dicionario para armazenar os dados dos restaurantes
    dados_restaurante = dict()
    # Para cada item no JSON
    for item in dados_json:
        # Separa o restaurante em uma variavel "nome_restaurante"
        nome_restaurante = item["Company"]
        # Se esse restaurante não estiver no dicionario criado
        if nome_restaurante not in dados_restaurante:
            # Cria em "dados_restaurante" uma chave que contém uma lista para depois pegar os items do restaurante
            dados_restaurante[nome_restaurante] = list()
            # Teremos o seguinte output como exemplo: {'Pizza Hut': []} -> 'Pizza Hut' = chave e a lista é o valor (que posteriormente conterá os items do restaurante)
        
        # Para cada restaurante criado, coletar as informações dos itens e adicionar na lista previamente criada
        dados_restaurante[nome_restaurante].append({
            "item": item["Item"],
            "price": item["price"],
            "description": item["description"]
        })
else:
    print(f"Erro foi: {response.status_code}")

# Para cada restaurante e dados dentro de dados_restaurante (pega chave / valor com .items())
for nome_restaurante, dados in dados_restaurante.items():
    # Atribui um nome de arquivo .json
    nome_arquivo = f"{nome_restaurante}.json"
    # Abre um arquivo com o nome do arquivo (em memória) em modo de escrita (write -> "w") e atribui um alias de "arquivo_restaurante"
    with open(nome_arquivo, "w") as arquivo_restaurante:
        # Com o modulo JSON importado, o metodo "dump" cria um JSON de acordo com o dados passados identando com 4 espaços
        json.dump(dados, arquivo_restaurante, indent=4)