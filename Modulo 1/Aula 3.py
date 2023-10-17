print("Pizzas disponíveis: Pepperoni, queijo e calabresa")
preco_pepperoni = 80.00
preco_queijo = 50.00
preco_calabresa = 70.00
total = 0
pedido_da_pizza = input("Escolha o sabor desejado: ").lower()
if pedido_da_pizza == "pepperoni" or pedido_da_pizza == "queijo" or pedido_da_pizza == "calabresa":
    if pedido_da_pizza == "pepperoni":
        print(f"O preço da pizza de Pepperoni é R${preco_pepperoni}")
        total = preco_pepperoni
    elif pedido_da_pizza == "queijo":
        print(f"O preço da pizza de Queijo é R${preco_queijo}")
        total = preco_queijo
    elif pedido_da_pizza == "calabresa":
        print(f"O preço da pizza de Calabresa é R${preco_calabresa}")
        total = preco_calabresa
    outra_pizza = input(("Deseja pedir outra pizza? S ou N?")).lower()
    if outra_pizza == "s":
        pedido_da_pizza_2 = input("Escolha o sabor desejado: ").lower()
        if pedido_da_pizza_2 == "pepperoni":
            print(f"O preço da pizza de Pepperoni é R${preco_pepperoni}")
            total = total + preco_pepperoni
            print(f"Pedido finalizado: Pizzas escolhidas {pedido_da_pizza} e {pedido_da_pizza_2}. Total do pedido R${total}")
        elif pedido_da_pizza_2 == "queijo":
            print(f"O preço da pizza de Queijo é R${preco_queijo}")
            total = total + preco_queijo
            print(f"Pedido finalizado: Pizzas escolhidas {pedido_da_pizza} e {pedido_da_pizza_2}. Total do pedido R${total}")
        elif pedido_da_pizza_2 == "calabresa":
            print(f"O preço da pizza de Calabresa é R${preco_calabresa}")
            total = total + preco_calabresa
            print(f"Pedido finalizado: Pizzas escolhidas {pedido_da_pizza} e {pedido_da_pizza_2}. Total do pedido R${total}")
        else:
            print(f"Pedido finalizado: Pizza escolhida {pedido_da_pizza}, segunda pizza não disponível. Total do pedido R${total}")
    else:
        print(f"Pedido finalizado: Pizza escolhida {pedido_da_pizza}. Total do pedido R${total}")
else:
    print("Pedido finalizado: Pizza não disponível")