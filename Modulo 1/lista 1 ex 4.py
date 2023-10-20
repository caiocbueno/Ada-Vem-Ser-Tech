"""Operadores
João é um empresário do ramo de construção civil e decidiu adotar novos critérios para dar reajuste salarial para seus funcionários
 quando completarem aniversário de contratação. Agora o reajuste vai ser dado seguindo as regras abaixo.

Tempo de serviço:

de 1 até 5 anos => 1%
de 6 até 10 anos => 1.5%
11 ou mais anos => 2% valor da inflação (IPCA)
O valor total percentual para o reajuste vai ser a soma do percentual de tempo de serviço + o percentual da inflação

Para ajudar a João a calcular o valor do reajuste salarial de seus funcionários crie uma função que recebe uma lista como entrada contendo apenas números decimais,
 onde a posição 0 da lista é o tempo de serviço, a posição 1 é o valor da inflação e a posição 2 é o salário do funcionário.
   Sua função deve calcular o novo salário e retorná-lo. Favor considerar arredondamento de duas casas decimais para o salário retornado.

Ex:
Entrada: [1, 5.0, 2000.00]
Saída: 2120.00

Ex:
Entrada: [11, 4.5, 2500.00]
Saída: 2662.50

A função deverá ser criada seguindo a estrutura abaixo:

def calculo_salario(lista):
    ### Seu código aqui

"""
def calculo_salario(lista):
	### Seu código aqui.
	salario = lista[2]
    
	if lista[0] > 0 and lista[0] < 6:
		salario += salario * ((1 + lista[1]) / 100)
	elif lista[0] >=6 and lista[0] < 11:
		salario += salario * ((1.5 + lista[1]) / 100)
	elif lista[0] >=11:
		salario += salario * ((2 + lista[1]) / 100)
	else:
		salario += salario * (lista[1] / 100)
	
	return round(salario, 2)


"""Resultados
Sucesso:

4
Falha:

2

Mostrar apenas falhas


Falha
Entrada:
[
  5.1,
  6.7,
  4500
]
Expectativa:
4869
Resultado:
4846.5


Sucesso
Entrada:
[
  1,
  5.7,
  4800
]
Expectativa:
5121.6
Resultado:
5121.6


Sucesso
Entrada:
[
  0,
  9.7,
  5000
]
Expectativa:
5485
Resultado:
5485


Falha
Entrada:
[
  10.1,
  4.7,
  4100
]
Expectativa:
4374.7
Resultado:
4354.2


Sucesso
Entrada:
[
  1,
  5,
  2000
]
Expectativa:
2120
Resultado:
2120


Sucesso
Entrada:
[
  11,
  4.5,
  2500
]
Expectativa:
2662.5
Resultado:
2662.5"""