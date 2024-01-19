class Pessoa:
    pessoas = list()
    def __init__(self, nome, idade, profissao):
        self._nome = nome.title()
        self._idade = int(idade)
        self._profissao = profissao.title()
        self._data_nascimento = 2024 - idade
        Pessoa.pessoas.append(self)
    
    def __str__(self):
        return f"{self._nome}: {self._idade} anos, {self._profissao}"
    
    @classmethod
    def mostrar_pessoas(cls):
        for pessoa in cls.pessoas:
            print(f"{pessoa._nome.ljust(15)} | {pessoa._profissao} | Nascido em {pessoa._data_nascimento} | {pessoa._idade} anos")

    def aniversario(self):
        self._idade = self._idade + 1

    def saudacao(self):
        print(f"Olá {self._nome}! Seja bem vindo ao seu novo trabalho como {self._profissao}")

lucas_carvalho = Pessoa("lucas carvalho", 24, "Analista de Suporte")

lucas_carvalho.aniversario()
Pessoa.mostrar_pessoas()

lucas_carvalho.saudacao()