from os import system

class ContaBancaria:
    contas = list()
    def __init__(self, titular, saldo, ativo=False):
        self._titular = titular.title()
        self._saldo = float(saldo)
        self._ativo = ativo
        ContaBancaria.contas.append(self)
    
    def __str__(self):
        return f"{self._titular}\nSaldo: {self._saldo}"
    
    @classmethod
    def mostrar_contas(cls):
        for conta in cls.contas:
            print(f"{conta._titular.ljust(15)}\nR$ {conta._saldo:.2f}\n{conta.ativo}\n\n")

    @property
    def ativo(self):
        return "✔" if self._ativo else "✖"
    
    def alterna_status_conta(self):
        self._ativo = not self._ativo

class ClienteBanco():
    lista_clientes = list()
    def __init__(self, nome, contato, conta, agencia=20, ativo=False):
        self._nome = nome.title()
        self._agencia = agencia
        self._conta = conta
        self._ativo = ativo
        self._contato = contato
        ClienteBanco.lista_clientes.append(self)

    def __str__(self):
        return f"{self._nome} está {self._ativo}"
    
    @classmethod
    def mostra_clientes(cls):
        for cliente in cls.lista_clientes:
            print(f"{"Nome:".ljust(10)} {cliente._nome}")
            print(f"{"Contato:".ljust(10)} {cliente._contato}")
            print(f"{"Ativo:".ljust(10)} {cliente.ativo}\n")

    @property
    def ativo(self):
        return "✔" if self._ativo else "✖"

conta_lucas = ContaBancaria("lucas oliveira carvalho", 1000)

ContaBancaria.mostrar_contas()
conta_lucas.alterna_status_conta()
ContaBancaria.mostrar_contas()

input("Enter para continuar...")
system("cls")


lucas = ClienteBanco(
    "Bob o Construtor",
    "bobconstrutor55@outlook.com",
    5485
)

ClienteBanco.mostra_clientes()