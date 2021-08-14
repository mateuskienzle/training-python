n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
fatorial = 1
print('Calculando {}! = ' .format(n), end='')
while c > 0:
    print('{}' .format(c), end='')
    if c > 1:
        print(' x ' , end='')
    else:
        print(' = ' , end='')
    fatorial *= c
    c -= 1
print('{}' .format(fatorial))