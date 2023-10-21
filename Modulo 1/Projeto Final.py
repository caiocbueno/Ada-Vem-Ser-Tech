print("SISTEMA DE GESTÃO DE RESTAURANTES")


def tela_incial():  # funcao pra tela inicial do programa
    while True:
        
        opcao_escolhida = int(input(("""
        Digite a opção desejada:

        1 - Gestão de restaurantes
        2 - Gestão de cardápio
        3 - Apresentação de informações
        4 - Encerrar programa
        """)))
        
        if opcao_escolhida == 1: # cada opçao escolhida encaminha para a respectiva funcao a ser criada
            gestao_restaurantes() 
        
        elif opcao_escolhida == 2:
            gestao_cardapios()
        
        elif opcao_escolhida == 3:
            apresentacao_de_informacoes()

        elif opcao_escolhida == 4:  # opcao 4 encerra o programa
            condicao = False
            print("Encerrando Programa")
            return condicao


def gestao_restaurantes():  # falta criar as outras funcoes, podemos dividir essa tarefa
    pass

def gestao_cardapios():
    pass

def apresentacao_de_informacoes():
    pass

# aqui começamos a executar o programa 

tela_incial() # executa a tela inicial