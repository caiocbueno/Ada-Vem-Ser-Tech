"""Enunciado
Substrings
Buscando se aperfeiçoar em soletração e na identificação de caracteres nas palavras, um aluno vencedor de uma gincana de soletração teve curiosidade em identificar as letras não repetidas de uma palavra. Para ajudá-lo no treino, crie uma função que recebe uma palavra e retorna o índice do primeiro caractere não repetido desta palavra. Caso não exista caractere único na palavra em questão, retornar -1.

Ex:
Entrada: amor
Saída: 0

Ex:
Entrada: cocada
Saída: 1
A função deverá ser criada seguindo a estrutura abaixo:

def primeiro_caractere_unico(palavra):
    ### Seu código aqui"""



def primeiro_caractere_unico(palavra):
	### Seu código aqui.
	for letra in palavra:
		if palavra.count(letra) == 1: # se o caractere é unico
			indice = palavra.index(letra) # variavel indice recebe o indice da letra
			break # sai do loop no primeiro caractere unico
		else: # se nao existe caractere unico
			indice = -1 # indice recebe -1
	return indice # retorna indice do primeiro caractere unico