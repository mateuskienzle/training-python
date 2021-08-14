n = float(input('Insira uma medida em metros para conversão:'))
c = n*100
m = n*1000
k = n/1000
print('a medida {}m em centímetros é {}cm; em milimetros é {}mm; em kilometros é {}km' .format(n, c, m, k))