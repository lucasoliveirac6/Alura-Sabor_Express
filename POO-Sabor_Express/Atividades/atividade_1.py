from os import system

class Musica:
    musicas = list()
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = int(duracao)
        Musica.musicas.append(self)
    
    def __str__(self):
        return f"{self.nome}"

    def mostra_musicas():
        for musica in Musica.musicas:
            print(f"{musica.nome} | {musica.artista} | {musica.duracao}")

who_says = Musica("Who Says", "Selena Gomez", 180)

Musica.mostra_musicas()
print(who_says)

input("Enter para continuar... ")
system("cls")