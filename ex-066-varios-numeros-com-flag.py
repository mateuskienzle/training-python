c = s = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        print(f'A soma dos {c} valores é {s}.')
        break
    s += n
    c += 1

''' Escrever "c = s = 0" é a mesma coisa que escrever:
c = 0
s = 0 '''