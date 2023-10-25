def substring_str(lista):
	lista_substrings = [] #lista vazia para armazenar a saída
	for palavra in lista: # primeiro for pega o primeiro item
		contador = 0 # define um contador de palavra
		for substrings in lista: #segundo for pega um item para comparacao
			if palavra in substrings: # se o a substring é encontrada
				contador += 1 # incrementa o contador
		if contador > 1: # se o contador é maior que 1, para não contar a própria palavra
			lista_substrings.append(palavra) # adiciona a palavra na lista de saída
	return lista_substrings # retorna a lista