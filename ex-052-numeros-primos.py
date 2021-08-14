import os
os.system("color")
n = int(input('Digite um número: '))
contador = 0
for c in range (1, n+1):
    if (n % c == 0):
        print('\033[33m', end= ' ')
        contador = contador + 1
    else:
        print('\033[31m', end= ' ')
    print('{}' .format(c), end= ' ')
print('\n\033[mO número {} foi divísivel {} vezes' .format(n, contador))
if contador > 2:
    print('Portanto, ele NÃO É PRIMO.')
else:
    print ('Portanto, ele É PRIMO.')
   