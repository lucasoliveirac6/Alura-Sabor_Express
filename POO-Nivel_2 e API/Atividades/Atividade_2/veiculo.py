class Veiculo:
    def __init__(self, marca, modelo, ligado=False):
        self._marca = marca
        self._modelo = modelo
        self._ligado = ligado
    
    def __str__(self):
        return f"Marca: {self._marca}\nModelo: {self._modelo}"