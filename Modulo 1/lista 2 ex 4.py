"""Enunciado
Operações Aritméticas
Uma professora decidiu premiar os melhores alunos de sua turma com um brinde. Para isso ela vai entregar um brinde
 para todos os alunos que tiverem uma média superior a média da turma.

Para ajudar o professor elabore uma função que recebe uma lista dos alunos em formato de dict (dicionário) 
com nome do aluno e a média do aluno. Esta função deve calcular a média da turma, identificar quais alunos tem média igual ou superior a média da turma
 e retornar uma lista com o nome dos alunos que possuem média igual ou superior a média da turma. A ordem dos nomes da lista de retorno deve obedecer a ordem da lista de entrada.

Ex:
Entrada: [{ "nome": "Maria", "nota": 7 },{"nome": "Marta", "nota": 5 },{"nome": "Marcia", "nota": 5.5 }]
Saída: [Maria]

Ex:
Entrada: [{ "nome": "Joao", "nota": 7 },{"nome": "Lucas", "nota": 5 },{"nome": "Maria", "nota": 0 },{"nome": "Marcia", "nota": 5.5 }]
Saída: [Joao, Lucas, Marcia]
A função deverá ser criada seguindo a estrutura abaixo:

def melhores_alunos(lista):
	### Seu código aqui"""






#lista = [{ "nome": "Maria", "nota": 7 },{"nome": "Marta", "nota": 5 },{"nome": "Marcia", "nota": 5.5 }]


def melhores_alunos(lista):

    lista_notas = []
    lista_melhores_alunos = []
    for item in lista:
        nota = item.get("nota")
        lista_notas.append(nota)
    #print(lista_notas)
    media = sum(lista_notas) / len(lista_notas)
    #print(media)

    for item in lista:
        nota = item.get("nota")
        if nota >= media:
            nome = item.get("nome")
            lista_melhores_alunos.append(nome)
    return lista_melhores_alunos