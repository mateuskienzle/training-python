from random import randint
from time import sleep
computador = randint(0, 5)
print('-=' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' *20)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)
if computador == jogador:
    print('Você acertou danadinho!')
else:
    print('Você errou hehe... eu pensei no número {} e não no {}.' .format(computador, jogador))
