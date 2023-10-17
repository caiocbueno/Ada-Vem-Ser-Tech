"""Enunciado
Operadores
Pedrinho trabalha com vendas de carro, mensalmente ele recebe um salário fixo e comissões baseadas em suas vendas. As comissões são as seguintes

Comissões:

5% sobre o valor total vendido no mês
valor fixo por cada carro vendido
Faça uma função que recebe uma lista com: número de carros por ele vendidos no mês, o valor total de suas vendas no mês, seu salário fixo, 
valor fixo que ele recebe por carro vendido. Calcule e retorne qual o salário dele (salário fixo mais comissões). Arredondar o valor de retorno para duas casas decimais.



Ex:
Entrada: [3, 20000.00, 2000.00, 250.00]
Saída: 3750.00

Ex:
Entrada: [4,25000.00, 3500.00, 100.00]
Saída: 5150.00



"""


def calculo_salario_com_comissao(lista):
	### Seu código aqui.
	comissao = lista[1]  * 0.05 #calculo 5% comissao
	
	salario = comissao + lista[2] + (lista[0]*lista[3]) #calculo salario
	#return salario
	
	#fiz assim primeiro, mas dava erro no resultado
	#por causa das casas decimais.
	
	#pesquisei como formatar corretamente e consegui resolver.
	salario = float(f"{salario:.2f}") #formata para duas casas decimais
									  #de acordo com o enunciado
									  #e converte novamente pra float.
	if salario.is_integer(): #se salário é inteiro
		return int(salario) #retorna o valor inteiro
	else: #se for decimal
		return salario #retorna o valor decimal