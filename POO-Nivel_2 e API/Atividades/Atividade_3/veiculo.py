from abc import ABC, abstractclassmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    @abstractclassmethod
    def ligar(self):
        pass
