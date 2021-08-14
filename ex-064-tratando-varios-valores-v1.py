c = 0
soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
if n == 999:
    print('Você digitou {} números e soma entre eles foi {}. ' .format(c, soma))

#NESSA EU FUI BRABO!!!