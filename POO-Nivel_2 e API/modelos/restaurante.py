from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = list()

    def __init__(self, nome, categoria):
        # '_' significa que é um atributo privado
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        # Não manipulado assim que se instancia um objeto
        self._avaliacao = list()
        self._cardapio = list()
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f"{self._nome} | {self._categoria}"
    
    #  Metodos da classe
    @classmethod
    def lista_restaurantes(cls):
        print("Restaurantes listados:\n")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo.ljust(20)}")

    # Modificar como o atributo vai ser lido com @property
    @property
    def ativo(self):
        return "✔" if self._ativo else "✖"
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_notas = len(self._avaliacao)

        return round(soma_notas / qtd_notas, 1)
    
    def adicionar_item_cardapio(self, item):
        if isinstance(item, ItemCardapio): # Se houver um item instanciado com aquele nome na classe especificada
            self._cardapio.append(item)

    @property # Um item que a gente quer ser capaz de ler, portanto, property
    def exibir_cardapio(self):
        print(f"Cardapio do restaurante {self._nome}\n")
        for i, item in enumerate(self._cardapio, start=1):
            #  Se tiver o atributo imprime de acordo com o tipo de item
            if hasattr(item, "_descricao"):
                mensagem_prato = f"Item {i}. Nome: {item._nome.ljust(15)} | Preço: R$ {f"{item._preco:.2f}".ljust(5)} | Descricao: {item._descricao}"
                print(mensagem_prato)
            else:
                mensagem_bebida = f"Item {i}. Nome: {item._nome.ljust(15)} | Preço: R$ {f"{item._preco:.2f}".ljust(5)} | Tamanho: {item._tamanho}"
                print(mensagem_bebida)
                