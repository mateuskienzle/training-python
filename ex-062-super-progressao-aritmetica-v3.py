print('Gerador de PA')
print('-=' *10)
n = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
c = 1
soma = n
total = 0
t = 10
while t != 0:
    total = total + t
    while c <= total:
        print('{}' .format(soma), end=' -> ')
        soma += r
        c += 1
    print('PAUSA')
    t = int(input('Quantos termos você quer mostrar mais? '))
print('Progressão finalizada com {} termos mostrados.' .format(total))