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

s = 'Nome:{0} \nSabor:{1}'

for dic in pedidos:
    print(s.format(dic['nome'],dic['sabor']))
