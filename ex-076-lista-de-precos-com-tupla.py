print('-' *40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' *40)
lista = ('Lápis', 'R$1.75',
        'Borracha', 'R$2.00',
        'Caderno', 'R$15.90',
        'Estojo', '25.00',
        'Transferidor', '4.20',
        'Compasso', '9.99',
        'Mochila', '120.32',
        'Canetas', '22.30',
        'Livro', '34.90')
for posicao in range (0, len(lista)):
    if posicao%2 == 0:
        print(f'{lista[posicao]:.<30}', end='')
    else:
        print(f'R${lista[posicao]:>7}')
    
        