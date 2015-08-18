pedidos = [
    {
        'nome' : 'Mario',
        'sabor' : 'portuguesaa'
    },
    {
        'nome' : 'Marco',
        'sabor' : 'mexicana'
    }
]

for dic in pedidos:
    print('Nome:{0} Sabor:{1}'.format(dic['nome'],dic['sabor']))
