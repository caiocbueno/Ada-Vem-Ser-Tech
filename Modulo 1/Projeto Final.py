print("SISTEMA DE GESTÃO DE RESTAURANTES")


def tela_incial():
    while True:
        
        opcao_escolhida = int(input(("""
        Digite a opção desejada:

        1 - Gestão de restaurantes
        2 - Gestão de cardápio
        3 - Apresentação de informações
        4 - Encerrar programa
        """)))
        
        if opcao_escolhida == 1:
            gestao_restaurantes()
        
        elif opcao_escolhida == 2:
            gestao_cardapios()
        
        elif opcao_escolhida == 3:
            apresentacao_de_informacoes()

        elif opcao_escolhida == 4:
            condicao = False
            print("Encerrando Programa")
            return condicao


def gestao_restaurantes():
    pass
def gestao_cardapios():
    pass
def apresentacao_de_informacoes():
    pass


tela_incial()