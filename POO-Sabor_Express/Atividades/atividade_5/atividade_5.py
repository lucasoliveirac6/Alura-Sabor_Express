class Livro:
    livros = list()
    def __init__(self, titulo, autor, ano_publicado, disponivel=True):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = disponivel
        Livro.livros.append(self)

    def __str__(self):
        return f"Livro: {self._livro}\nAutor: {self._autor}\nAno: {self._ano_publicado}"
    
    @staticmethod
    def verifica_disponibilidade(ano):
        return [livro for livro in Livro.livros if livro._ano_publicado == ano and livro._disponivel]
        # print(f"Livros de {ano}:\n")
        # for livro in Livro.livros:
        #     if livro._disponivel and livro._ano_publicado == ano:
        #         print(f"{"Título:".ljust(10)} {livro._titulo}")
        #         print(f"{"Autor:".ljust(10)} {livro._autor}\n")

    @property
    def disponivel(self):
        return "Disponivel" if self._disponivel else "Indisponivel."
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor

    def emprestar_livro(self):
        self._disponivel = False
        print(f"{self._titulo} emprestado. {self.disponivel}")


