class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

class Restaurante:
    def __init__(self, nome, tipo, ano_fundacao, renda):
        self.nome = nome
        self.tipo = tipo
        self.ano_fundacao = int(ano_fundacao)
        self.renda = float(renda)
        self.ativo = False

    def __str__(self):
        return f"{self.nome} | {self.tipo}"

class Cliente:
    def __init__(self, nome, email, telefone, tipo):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.tipo = tipo
    
    def __str__(self):
        return self.tipo


la_guapa = Restaurante("La Guapa", "Empanadas", 1999, 5000.12)
romero_brito = Cliente("Romero Brito", "romero@brito.com.br", "11912344567", "VIP")

print(f"{la_guapa}\n")
print(f"{romero_brito}\n")