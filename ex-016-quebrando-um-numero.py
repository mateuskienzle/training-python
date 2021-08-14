from math import trunc
n = float(input('Digite um valor:'))
print ('O valor digitado é {} e a sua porção inteira é {}' .format(n, trunc(n)))



#outra formar de fazer esse mesmo código, porém sem precisar importar o módulo math.
'''n = float(input('Digite um valor:'))
print ('O valor digitado é {} e a sua porção inteira é {}' .format(n, int(n)))'''