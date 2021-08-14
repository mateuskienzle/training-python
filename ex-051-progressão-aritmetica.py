print('-=' *22)
print('CALCULANDO OS 10 PRIMEIROS TERMOS DE UMA P.A')
print('-=' *22)
n = int(input('Primeiro termo da PA: '))
r = int(input('Razão: '))
décimo_termo_PA = (n+(10-1)*r)
for c in range(n, décimo_termo_PA +r, r):
    print('{}'.format(c), end =' -> ')
print('Acabou')