class Restaurante:
    restaurantes = list()

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        # _ativo significa que é um atributo privado
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f"{self._nome} | {self._categoria}"
    
    #  Metodos da classe
    @classmethod
    def lista_restaurantes(cls):
        print("Restaurantes listados:\n")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo.ljust(20)}")

    # Modificar como o atributo vai ser lido com @property
    @property
    def ativo(self):
        return "✅" if self._ativo else "❌"
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    

restaurante_praca = Restaurante("Pracinha Show", "Fast Food")
restaurante_pizza = Restaurante("Sao Joao das Pizzas", "Pizzaria")


# print(restaurante_praca)
# print(restaurante_pizza)

Restaurante.lista_restaurantes()