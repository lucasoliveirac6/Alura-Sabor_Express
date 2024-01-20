from fastapi import FastAPI,Query
import requests

app = FastAPI()

@app.get("/api/hello")
def hello_world():
    """
    Endpoint que exibe uma mensagem incrível no mundo da programação
    """
    return {"Hello":"World!"}


# Criar uma rota para quando requisitarmos a pagina /api/restaurantes/ (A barra no fim da string significa que estamos antecipando uma entrada de um parâmetro)
@app.get("/api/restaurantes/")
# definir a função de retornar os restaurantes apontando que queremos o "restaurante", ele será uma "str" em que a Query se não passado nada retornará "None".
# Isso significa que se entrado em /api/restaurantes/ o valor padrão é None
def get_restaurantes(restaurante: str = Query(None)):
    """
    Endpoint para ver os cardápios dos restaurantes
    """
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    # Pegar as informações = get
    response = requests.get(url=url)
    # Se conseguir captar os dados (status == 200) continua
    if response.status_code == 200: 
        # Pega os dados do JSON que foi respondido
        dados_json = response.json()

        # Se a query passada retornar None
        if restaurante is None:
            # Retorna todos os dados dos restaurantes
            return {"Dados":dados_json}
        
        # Cria uma lista para armazenar os dados dos restaurantes caso um parâmetro tenha sido passado
        dados_restaurante = list()

        # Para cada item no JSON
        for item in dados_json:
            # Se o item do JSON for equivalente ao restaurante que foi passado
            if item["Company"] == restaurante:       
                # Para cada restaurante criado, coletar as informações dos itens e adicionar na lista previamente criada
                dados_restaurante.append({
                    "item": item["Item"],
                    "price": item["price"],
                    "description": item["description"]
                })
        # Retorna o nome do restaurante e os itens deste respectivo restaurante
        return {"Restaurante":restaurante,"Items":dados_restaurante}
    else:
        # Se tudo der errado, retorna a mensagem de erro com o status e o texto do status.
        return{"Erro":f"{response.status_code} - {response.text}"}