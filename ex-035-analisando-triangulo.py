print('-=' *15)
print('Analisador de Triângulos')
print('-=' *15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
if a>b and a<c or a<b and a>c:
    medio = a
if b>a and b<c or b<a and b>c:
    medio = b
if c>a and c<b or c<a and c>b:
    medio = c
if menor + medio > maior:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')


'''poderia ter feito esse mesmo programa de uma forma muito mais simples:
if a<b+c and b<a+c and c<a+b:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')'''
