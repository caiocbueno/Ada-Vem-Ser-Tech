print("SISTEMA DE GESTÃO DE RESTAURANTES")

opcao_escolhida = None # variável global que será usada nas funções
lista_restaurantes = []


def opcao():
    """Função de múltipla escolha retornando um número inteiro"""
    global opcao_escolhida # vamos usar a variável global para poder ser acessada em outras funções
    opcao_escolhida = int(input("Digite a opção desejada: "))
    return opcao_escolhida #retorna a opcao escolhida

def tela_incial():  # funcao para a tela inicial do programa
    while True:
        print(("""
        1 - Gestão de restaurantes
        2 - Gestão de cardápio
        3 - Visualizar informações (Restaurantes e cardápios)
        4 - Encerrar programa
        """))

        opcao() # chama a função de múltipla escolha
        
        if opcao_escolhida == 1: # compara a opção escolhida e seleciona a respectiva função
            gestao_restaurantes() 
        
        elif opcao_escolhida == 2:
            gestao_cardapios()
        
        elif opcao_escolhida == 3:
            apresentacao_de_informacoes()

        elif opcao_escolhida == 4:  # opcao 4 encerra o programa
            condicao = False
            print("Encerrando programa")
            return condicao # retorna a condição False para sair do loop e encerrar o programa


def gestao_restaurantes(): 
    """Função menu de gerenciamento dos restaurantes"""
    while True:
        print(("""
        1 - Adicionar restaurante
        2 - Editar restaurante
        3 - Remover restaurante
        4 - Voltar para a tela inicial
        """))
        
        opcao()
            
        if opcao_escolhida == 1: # cada opçao escolhida encaminha para a respectiva funcao a ser criada
                print("Adicionar restaurante") 
                adicionar_restaurante()

        elif opcao_escolhida == 2:
                print("Editar restaurante")
            
        elif opcao_escolhida == 3:
                print("Remover restaurante")

        elif opcao_escolhida == 4:  # opcao 4 encerra o programa
                condicao = False
                print("Voltando para tela inicial")
                return condicao
    

def gestao_cardapios():
    while True:
        print(("""
        1 - Adicionar item ao cardápio
        2 - Editar item do cardápio
        3 - Remover item do cardápio
        4 - Voltar para a tela inicial
        """))
        
        opcao()
            
        if opcao_escolhida == 1: # cada opçao escolhida encaminha para a respectiva funcao a ser criada
                print("Adicionar item ao cardápio") 
            
        elif opcao_escolhida == 2:
                print("Editar item do cardápio")
            
        elif opcao_escolhida == 3:
                print("Remover item do cardápio")

        elif opcao_escolhida == 4:  # opcao 4 encerra o programa
                condicao = False
                print("Voltando para tela inicial")
                return condicao

def apresentacao_de_informacoes():
    while True:
        print(("""
        1 - Exibir lista de restaurantes
        2 - Voltar para a tela inicial
        """))
        
        opcao()
            
        if opcao_escolhida == 1: # cada opçao escolhida encaminha para a respectiva funcao a ser criada
                print("Exibir lista de restaurantes") 
                exibir_restaurantes()

        elif opcao_escolhida == 2:
                condicao = False
                print("Voltando para tela inicial")
                return condicao
        
def adicionar_restaurante():
    while True:
        nome = input("Digite o nome do restaurante: ")
        lista_restaurantes.append(nome)
        telefone = input("Digite o telefone do restaurante: ")
        lista_restaurantes.append(telefone)
        print(lista_restaurantes)
        condicao = False
        return lista_restaurantes, condicao

def exibir_restaurantes():
        print("Lista de restaurantes")


# aqui começamos a executar o programa 

tela_incial() # executa a tela inicial