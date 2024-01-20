from os import system
from carro import Carro

carro1 = Carro(marca="Ford", modelo="Focus", cor="Preto")
carro2 = Carro(marca="Chevrolet", modelo="Cruze", cor="Prata")
carro3 = Carro(marca="Honda", modelo="Civic", cor="Vermelho")

def main():
    print(f"Carro 1: {carro1._marca} {carro1._modelo}, Cor: {carro1._cor}")
    print(f"Carro 2: {carro2._marca} {carro2._modelo}, Cor: {carro2._cor}")
    print(f"Carro 3: {carro3._marca} {carro3._modelo}, Cor: {carro3._cor}")

if __name__ == "__main__":
    main()