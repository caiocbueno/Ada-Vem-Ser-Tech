"""Listas
Analisando as temperaturas do ano passado, Paulinho busca identificar quais dias houveram temperaturas médias únicas diferentes do restante dentro da mesma semana. 
Dada uma lista de decimais (temperaturas) como entrada, onde existe um único número distinto nesta lista e os demais são repetidos (uma ou mais vezes), 
crie uma função para encontrar o número que é unico e retorná-lo.

Ex:
Entrada: [18, 19, 20, 21, 20, 19, 18]
Saída: 21

Ex:
Entrada: [28.5, 27.9, 28.5, 27.9, 30, 28.5]
Saída: 30"""

entrada = [28.5, 27.9, 28.5, 27.9, 30, 28.5]
for numero in entrada:
    if entrada.count(numero) == 1:
        print(numero)
