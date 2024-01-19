import os

restaurantes = [
    {"nome": "Pizza Plannet", "categoria": "Pizzaria", "ativo": False},
    {"nome": "Burger King", "categoria": "Hamburgueria", "ativo": False},
    {"nome": "Sushilandia", "categoria": "Japonesa", "ativo": False}
]


def exibe_opcoes():
    """ Função responsável por exibir todas as opções
    
    Outputs:
    - Opções do programa

    """
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def finalizar_app():
    """Função que finaliza o aplicativo"""
    exibir_subtitulos("Finalizando app...")

def opcao_invalida():
    """Função que sinaliza opções invalidas do menu"""
    print("Opção invalida!")
    voltar_menu_principal()

def cadastrar_novo_restaurante():
    """Função que cadastra um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Cadastra o restaurante na lista de restaurantes
    
    """
    exibir_subtitulos("Cadastro de novos restaurantes")

    dados_restaurante = {
        "nome": input("Nome do restaurante: "),
        "categoria": input("Categoria do restaurante: "),
        "ativo": False
    }

    restaurantes.append(dados_restaurante)
    

    print(f"Restaurante {dados_restaurante["nome"]} cadastrado com sucesso!")

    voltar_menu_principal()
    
def mostrar_restaurantes():
    """Função que exibe todos os restaurantes cadastrados
    
    Outputs:
    - Mostra a lista de todos os restaurantes cadastrados
    
    """
    exibir_subtitulos("Restaurantes cadastrados:")

    for restaurante in restaurantes:
        for key, value in (restaurante.items()):
            if key == "ativo":
                status = "Ativo" if value else "Inativo"
                print(f"{key.upper().ljust(10)}: {status}")
            else:
                print(f"{key.upper().ljust(10)}: {value}")
        print()

    voltar_menu_principal()

def alternar_estado_restaurante():
    """Função que altera o status de um restaurante entre ativo e inativo
    
    Inputs:
    - Nome do restaurante

    Outputs:
    - Alterna o status do restaurante entre Ativo e Inativo
    
    """
    exibir_subtitulos("Alterando estado do restaurante:")

    nome_restaurante = input("Restaurante a ser ativado:")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not(restaurante["ativo"])
            mensagem = f"Restaurante {nome_restaurante} foi ativado" if restaurante["ativo"] else f"Restaurante {nome_restaurante} foi desativado"
            print(mensagem)
    if not restaurante_encontrado:
        print(f"Restaurante {nome_restaurante} não encontrado")

    voltar_menu_principal()

def escolher_opcoes():
    """Função que gere as opções escolhidas pelo usuário
    
    Inputs:
    - Opção escolhida

    Outputs:
    - Retorna a função responsável por aquela opção escolhida

    """
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        # if opcao_escolhida == 1:
        #     print(f"Cadastrar restaurante")
        # elif opcao_escolhida == 2:
        #     print(f"Listar restaurantes")
        # elif opcao_escolhida == 3:
        #     print(f"Ativar restaurantes")
        # else:
        #     finalizar_app()

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                mostrar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
    except:
        opcao_invalida()
        
def exibe_nome_programa():
    """Função que exibe o nome do programa"""
    print("Sabor Express")

def voltar_menu_principal():
    """Função que volta ao menu principal"""
    input("\nPressione enter para continuar ")
    main()

def exibir_subtitulos(texto):
    """Função que mostra os subtitulos com a mensagem de texto especificada"""
    os.system("cls")
    linha = "*" * len(texto)
    print(linha)
    print(f"{texto}")
    print(f"{linha}\n")

def main():
    """Função principal do programa"""
    os.system("cls")
    exibe_nome_programa()
    exibe_opcoes()
    escolher_opcoes()

if __name__ == "__main__":
    main()