from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Pracinha da Serra", "Gourmet")
restaurante_mexicano = Restaurante("Tamaexico", "Mexicano")
restaurante_esquina = Restaurante("Esquininha da Vó", "Japonesa")

restaurante_mexicano.alternar_estado()
restaurante_mexicano.receber_avaliacao("Lucas", 3)
restaurante_mexicano.receber_avaliacao("Joao", 2)
restaurante_mexicano.receber_avaliacao("Alberto", 5)



def main():
    Restaurante.lista_restaurantes()


if __name__ == "__main__":
    main()