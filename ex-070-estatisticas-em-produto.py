c = total = produto_mais_de10000 = mais_barato = 0
item_mais_barato = ' '
print('-' *35)
print('\tLOJA SUPER BARATÃO')
print('-' *35)
while True:
    produto = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$'))
    total += preco
    c += 1
    if preco > 1000:
        produto_mais_de10000 += 1
    if c == 1 or preco < mais_barato:
        mais_barato = preco
        item_mais_barato = produto
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar [S/N]? ')).upper()[0]
    if pergunta == 'N':
        break
print('{:-^40}' .format('FIM DO PROGRAMA'))
print(f'O total da compra foi: {total:.2f}')
print(f'Temos {produto_mais_de10000} produtos custando mais de R$1000.00.')
print(f'O produto mais barato foi {item_mais_barato} e custou R${mais_barato:.2f}')


'''
OBS: O "{:-^40}" utilizado no campo= print('{:-^40}' .format('FIM DO PROGRAMA')) serve para centralizar o texto 
desse print e inserir o texto FIM DO PROGRAMA dentro dos ---.'''