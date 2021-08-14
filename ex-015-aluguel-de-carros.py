d = float(input('Quantos dias alugados?'))
k = float(input('Quantos Km rodados?'))
pd = d*60
pk = k*0.15
print('O total a pagar é de R${:.2f}' .format(pd+pk))