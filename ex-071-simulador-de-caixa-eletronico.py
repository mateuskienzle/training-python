print('=' *30)
print('{:^30}'.format('BANCO DO TEUZI'))
print('=' *30)
n = int(input('Que valor você quer sacar? R$'))
c50 = c20 = c10 = c1 = valor50 = valor20 = valor10 = valor1 = 0
while True:
    c50 += 1 
    if (c50*50) > n:
        c50 -= 1
        valor50 = n - (c50*50)
        break
while True:
    c20 += 1
    if (c20*20) > valor50:
        c20 -= 1
        valor20 = valor50 - (c20*20)
        break
while True:
    c10 += 1
    if (c10*10) > valor20:
        c10 -= 1
        valor10 = valor20 - (c10*10)
        break
while True:
    c1 += 1
    if (c1*1) > valor10:
        c1 -= 1
        valor1 = valor10 - (c1*1)
        break
if c50 !=0:
    print(f'Total de {c50:2} cédulas de R$50')
if c20 !=0:
    print(f'Total de {c20:2} cédulas de R$20')
if c10 != 0:
    print(f'Total de {c10:2} cédulas de R$10')
if c1 !=0 :
    print(f'Total de {c1:2} cédulas de R$1')
print('=' *30)
print('Volte sempre ao BANCO DO TEUZI ;)')