class Restaurante:
    restaurantes = list()

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    
    def lista_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {"Ativo" if restaurante.ativo else "Inativo"}")
    

restaurante_praca = Restaurante("Pracinha Show", "Fast Food")
restaurante_pizza = Restaurante("Sao Joao das Pizzas", "Pizzaria")


# print(restaurante_praca)
# print(restaurante_pizza)

Restaurante.lista_restaurantes()