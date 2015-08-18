pedidos = []


def adiciona_pedido(nome, sabor, observacao=None):
    pedido = {}
    pedido['nome'] = nome
    pedido['sabor'] = sabor
    pedido['observacao'] = observacao

    return pedido


pedidos.append(adiciona_pedido('omar', 'jawaiana'))
pedidos.append(adiciona_pedido('mary', 'napolitana', 'pouco queijo'))

template = '\nNome: {nome}\nSabor: {sabor}'
for ped in pedidos:
    print(template.format(**ped))
    if ped['observacao']:
        print('Observacao: {0}'.format(ped['observacao']))
    print('-'*20)    
