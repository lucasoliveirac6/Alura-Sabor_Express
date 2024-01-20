from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, nome, modelo, portas):
        super().__init__(nome, modelo)
        self._portas = int(portas)

    def __str__(self):
        return f"{super().__str__()}\nPortas: {self._portas}\nStatus: {"Ligado" if self._ligado else "Desligado"}\n"