import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hip = math.hypot(co, ca)
print('A hipotenusa mede: {:.2f}' .format(hip))




#outra formar de fazer esse mesmo código, porém sem precisar importar o módulo math.
'''co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hip = ((co**2)+(ca**2))**(1/2)
print('A hipotenusa mede: {:.2f}' .format(hip))'''