from os import system
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante("Pracinha da Serra", "Gourmet")
suco_laranja = Bebida("Suco de laranja", 5, "Grande")
pao_de_queijo = Prato("Pão de queijo", 3.50, "O melhor pão de queijo")

restaurante_praca.adicionar_item_cardapio(suco_laranja)
restaurante_praca.adicionar_item_cardapio(pao_de_queijo)



def main():
    print("Antes do desconto")
    restaurante_praca.exibir_cardapio
    suco_laranja.aplicar_desconto()
    pao_de_queijo.aplicar_desconto()
    print("\nDepois do desconto")
    restaurante_praca.exibir_cardapio

    input("Enter para continuar...")
    system("cls")

if __name__ == "__main__":
    main()