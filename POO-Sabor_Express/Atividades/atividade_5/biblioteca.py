# referente a atividade_5
from atividade_5 import Livro


pjo1 = Livro("Percy Jackson e ladrão de raios", "Rick Ryordan", 2008)
pjo2 = Livro("Percy Jackson e o mar de monstros", "Rick Ryordan", 2010)
pjo3 = Livro("Percy Jackson e a maldição do titã", "Rick Ryordan", 2010)
pjo4 = Livro("Percy Jackson e a batalha do labirinto", "Rick Ryordan", 2012)
pjo5 = Livro("Percy Jackson e o último olimpiano", "Rick Ryordan", 2015)


for livro in Livro.verifica_disponibilidade(2010):
    print(f"{"Título:".ljust(10)} {livro.titulo}")
    print(f"{"Autor:".ljust(10)} {livro.autor}\n")