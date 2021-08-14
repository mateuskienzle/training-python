from random import randint
from time import sleep
numeros = list()
jogos = list()
print('-' *30)
print('{:^30}' .format('JOGA NA MEGA SENA'))
print('-' *30)
quant = int(input('Quantos jogos você quer sortear? '))
print('=-'*3, (f'SORTEANDO {quant} JOGOS'), '=-' *3)
total = 1
while total <= quant:
    cont = 0
    while True:
            n = randint(1, 60)
            if n not in numeros:
                numeros.append(n)
                cont += 1
            if cont >= 6:
                break
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
    total += 1
for i, v in enumerate(jogos):
    print(f'Jogo {i+1}: {v}')
    sleep(1)