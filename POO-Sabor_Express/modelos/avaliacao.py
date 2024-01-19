class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        if 0 <= nota <= 10:
            self._nota = nota