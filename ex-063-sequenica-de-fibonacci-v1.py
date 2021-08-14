print('-' *25)
print('Sequência de Fibonacci')
print('-' *25)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' *35)
print('{} -> {}' .format(t1, t2), end =' -> ')
c = 3
while c <= n:
    t3 = t1 + t2
    print('{}' .format(t3), end =' -> ')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')