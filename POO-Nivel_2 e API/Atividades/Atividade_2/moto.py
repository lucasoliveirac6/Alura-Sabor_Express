from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self):
        return f"{super().__str__()}\nTipo: {self._tipo}\nStatus: {"Ligado" if self._ligado else "Desligado"}\n"