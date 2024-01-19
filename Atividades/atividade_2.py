import os
# Exercicio 1
# Par ou ímpar

num = int(input("Numero: "))

if num % 2 == 0:
    os.system("cls")
    print(f"Número {num} é par")
else:
    os.system("cls")
    print(f"Número {num} é ímpar")

# Exercicio 2
# Classificar idades

age = int(input("Age: "))
if 0 <= age <= 12:
    print(f"Se trata de uma criança de {age} anos")
elif 13 <= age <=18:
    print(f"Se trata de um adolescente de {age} anos")
else:
    print(f"Se trata de um adulto de {age} anos")

# Exercicio 3
# Validador de senha
    
pwd = input("Senha: ")
if len(pwd) < 6:
    print("Senha muito curta.")

# Exercicio 4
# Quadrante dos planos cartesianos
    
x = int(input("Coordenada X: "))
y = int(input("Coordenada Y: "))

if x > 0 and y > 0:
    print("Primeiro quadrante")
elif x < 0 and y > 0:
    print("Segundo quadrante")
elif x == 0 and y == 0:
    print("Terceiro quadrante")
elif x > 0 and y < 0:
    print("Quarto quadrante")
else:
    print("Ponto no eixo de origem")