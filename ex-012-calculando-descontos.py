p=float(input('Qual é o salário do funcionário? R$'))
s = p*1.15
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}' .format(p, s))