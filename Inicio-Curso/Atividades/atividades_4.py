import os

def clear_screen():
    input("Enter para continuar... ")
    os.system("cls")


# Informações pessoa

pessoa = {
    "nome": "Lucas",
    "idade": 24,
    "cidade": "Itatiba"
}

print(f"Idade de {pessoa["nome"]} é {pessoa["idade"]}\n")
# pessoa.update({"idade": 25})
pessoa["idade"] = 25
print(f"Idade de {pessoa["nome"]} é {pessoa["idade"]}\n")

numeros = dict()
for i in range(1, 5):
    numeros[i] = i**2
print(numeros)

chave = input("Chave: ")
if chave in pessoa.keys():
    print(f"Pessoa contem chave: {chave}")
else:
    print(f"Pessoa NÃO contem chave: {chave}")

clear_screen()

frequencia = dict()
frase = input("Frase: ").split(" ")

for palavra in frase:
    if list(frequencia.keys()).count(palavra) == 0:
        frequencia[palavra] = frase.count(palavra)

print(frequencia)