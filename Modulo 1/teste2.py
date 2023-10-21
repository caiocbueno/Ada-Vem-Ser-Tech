print("SISTEMA DE GESTÃO DE RESTAURANTES")

opcao_escolhida = "teste"
def opcao():
    
    opcao_escolhida = input("Digite a opção desejada: ")
    return opcao_escolhida

opcao()
print(opcao_escolhida)

if opcao_escolhida == 5:
    print("if ok")