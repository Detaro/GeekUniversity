# Criando a lista tarefas
tarefas = []
pedfinalizado = 0
# Usando o Input() vamos coletar do usuário qual a tarefa a ser adicionada.
while not pedfinalizado == 'S':
    atividade = input('Insira uma atividade: ')
    tarefas.append(atividade)
    pedfinalizado = str(input('Finalizar pedido? S/N: ')).upper()
#Adiciona a tarefa indicada pelo usuário a lista de tarefas




print(tarefas)