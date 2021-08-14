preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO:')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opção = int(input('Qual é a opção? '))
if opção == 1:
    desconto = preço*0.9
    print('Sua compra de {} vai custar {:.2f} no final.' .format(preço, desconto))
elif opção == 2:
    desconto = preço*0.95
    print('Sua compra de {} vai custar {:.2f} no final.' .format(preço, desconto))
elif opção == 3:
    parcelas = (preço/2)
    print('Sua compra será parcelada em 2x de {:.2f} sem juros.' .format(parcelas))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = preço*1.2
    n_parcelas = (juros/parcelas)
    print('Sua compra será parcelada em {}x de {:.2f} com juros.' .format(parcelas,n_parcelas))
    print('Sua compra de {} vai custar {:.2f} no final.' .format(preço, juros))
else:
    print('Opção de pagamento inválida!')

