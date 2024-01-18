import math

print("Sabor Express")

print("1. Cadastrar restaurante")
print("2. Listar restaurante")
print("3. Ativar restaurante")
print("4. Sair\n")

opcao_escolhida = int(input("Escolha uma opção: "))

print(f"Você escolheu a opção {opcao_escolhida}")

if opcao_escolhida == 1:
    print(f"Cadastrar restaurante")
elif opcao_escolhida == 2:
    print(f"Listar restaurantes")
elif opcao_escolhida == 3:
    print(f"Ativar restaurantes")
else:
    print(f"Encerrando o programa.")