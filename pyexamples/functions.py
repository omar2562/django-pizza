pedidos = []


def adiciona_pedido(nome, sabor):
    pedido = {}
    pedido['nome'] = nome
    pedido['sabor'] = sabor

    pedidos.append(pedido)


print (pedidos)
adiciona_pedido('omar', 'jawaiana')
adiciona_pedido('mary', 'napolitana')
print (pedidos)
