# resolução professor

pizzas_disponiveis = "pepperoni, queijo e calabresa"

preco_calabresa = 70.0
preco_queijo = 50.0
preco_pepperoni = 80.0

quantidade_calabresa = 0
quantidade_queijo = 0
quantidade_pepperoni = 0

condicao = True
pizza_pedida = " "
valor_total = 0

while condicao:
    pizza_pedida = input("Qual pizza você gostaria?")
    
    if pizza_pedida == "pepperoni" or pizza_pedida == "queijo" or pizza_pedida == "calabresa":
        
        if pizza_pedida == "calabresa":
            quantidade_calabresa += 1
            valor_total += 70.0
        elif pizza_pedida == "queijo":
            quantidade_queijo += 1
            valor_total += 50.0
        elif pizza_pedida == "pepperoni":
            quantidade_pepperoni += 1
            valor_total += 80.0
        
        resposta = " "
        while resposta != "s" and resposta != "n":
            resposta = input("Você deseja outra pizza? (S/N)")
            if resposta.lower() == "s":
                condicao = True  
            elif resposta.lower() == "n":
                condicao = False    
            else:
                print("valor incorreto")
                condicao = True
    else:
        condicao = False
        
        print("Encerrando o programa")
        
if quantidade_calabresa > 0 or quantidade_pepperoni > 0 or quantidade_queijo > 0:        
    print("Calabresa: ", quantidade_calabresa)
    print("Queijo: ", quantidade_queijo)
    print("Pepperoni: ", quantidade_pepperoni)
    print("Valor Total: ", valor_total)
else:
    print("Pedido inválido")