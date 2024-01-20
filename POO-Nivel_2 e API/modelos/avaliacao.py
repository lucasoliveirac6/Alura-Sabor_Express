class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota
        if not 0 <= nota <= 5:
            raise Exception("Nota deve estar entre 0 e 5")