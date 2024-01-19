import os

def clear_screen():
    input("\nEnter para continuar")
    os.system("cls")

# Listas com diferentes informações

numbers = [i for i in range(1, 11)]
names = ["Lucas", "Marcela", "Otavio", "Erika"]
years = [1999, 2024]

# Percorrendo elementos da lista
print("Numeros:")
for num in numbers:
    print(num)
print("\nNomes:")
for name in names:
    print(name)
print("\nAnos:")
for yaear in years:
    print(yaear)
clear_screen()

# Somando numeros ímpares
print("Soma dos números:\n")
soma = 0
for num in numbers:
    if num % 2 != 0:
        soma += num
print(soma)
clear_screen()

# Ordem decrescente dos numeros
print("Ordem decrescente:\n")
numbers.sort(reverse=True)
for num in numbers:
    print(num)
clear_screen()

# Tabuada
try:
    number = int(input("Tabuada do numero: "))
    for i in range(0, 11):
        print(f"{number} x {i} = {number*i}")
    clear_screen()
except:
    print("Nenhum número selecionado")
    clear_screen()

# Lista de numeros
numbers = list()
sum = 0
for i in range(0, 10):
    try:
        numbers.append(int(input(f"Digite o número {i}: ")))
    except:
        os.system("cls")
        print("Numero inválido. Finalizando o programa...\n")
        exit(1)
for num in numbers:
    sum += num
print(f"\nSoma dos números é: {sum}")

# Media dos valores da lista
try:
    media = sum / len(numbers)
    print(f"Média dos números é: {media:.2f}")
    clear_screen()
except ZeroDivisionError:
    print("Lista vazia")
    clear_screen()