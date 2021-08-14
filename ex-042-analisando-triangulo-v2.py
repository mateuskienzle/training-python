a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a<b+c and b<a+c and c<a+b:
    if a==b !=c or a==c !=b or c==b !=a:
        tipo = 'Isósceles'
    elif a==b==c:
        tipo = 'Equilátero'
    elif a != b != c:
        tipo = 'Escaleno'
    print('Os segmentos acima podem formar um triângulo {}.' .format(tipo))
else:
    print('Os segmentos acima não podem formar um triângulo!')