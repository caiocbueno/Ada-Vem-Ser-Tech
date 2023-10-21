print("SISTEMA DE GESTÃO DE RESTAURANTES")

opcao_escolhida = None

def opcao():
    global opcao_escolhida
    opcao_escolhida = int(input("Digite a opção desejada: "))
    return opcao_escolhida

def tela_incial():  # funcao pra tela inicial do programa
    while True:
        print(("""
        1 - Gestão de restaurantes
        2 - Gestão de cardápio
        3 - Visualizar informações (Restaurantes e cardápios)
        4 - Encerrar programa
        """))

        opcao()
        
        if opcao_escolhida == 1: # cada opçao escolhida encaminha para a respectiva funcao a ser criada
            gestao_restaurantes() 
        
        elif opcao_escolhida == 2:
            gestao_cardapios()
        
        elif opcao_escolhida == 3:
            apresentacao_de_informacoes()

        elif opcao_escolhida == 4:  # opcao 4 encerra o programa
            condicao = False
            print("Encerrando programa")
            return condicao


def gestao_restaurantes():  # falta criar as outras funcoes, podemos dividir essa tarefa
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
            
        elif opcao_escolhida == 2:
                condicao = False
                print("Voltando para tela inicial")
                return condicao
        

# aqui começamos a executar o programa 

tela_incial() # executa a tela inicial