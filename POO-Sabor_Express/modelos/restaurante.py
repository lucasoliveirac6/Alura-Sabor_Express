from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = list()

    def __init__(self, nome, categoria):
        # '_' significa que é um atributo privado
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        # Não manipulado assim que se instancia um objeto
        self._avaliacao = list()
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
            return 0
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_notas = len(self._avaliacao)

        return round(soma_notas / qtd_notas, 1)