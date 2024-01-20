# Importanto metodos para tornar uma classe abstrata
from abc import ABC, abstractclassmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = float(preco)

    @abstractclassmethod # Todas as classes derivadas precisam deste método
    def aplicar_desconto(self):
        pass 
        # O método se torna obrigatorio para todas as classes que derivam a classe mãe, mas independe de como ela é implementada no código