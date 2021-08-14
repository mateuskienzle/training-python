from random import choice
from time import sleep
import sys
print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
lista = ['pedra', 'papel', 'tesoura']
jogada = int(input('Qual é a sua jogada? '))
if jogada == 0:
    escolha = 'pedra'
elif jogada == 1:
    escolha = 'papel'
elif jogada == 2:
    escolha = 'tesoura'
else:
    print('Jogada inválida!')
    sys.exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
computador = choice(lista)
print('-=' *12)
print('Computador jogou {}' .format(computador))
print('Jogador jogou {}' .format(escolha))
print('-=' *12)
if computador == 'pedra' and jogada == 1:
    print('Jogador venceu!')
elif computador == 'pedra' and jogada == 2:
    print('Computador venceu!')
elif computador == 'papel' and jogada == 0:
    print('Computador venceu!')
elif computador == 'papel' and jogada == 2:
    print('Jogador venceu!')
elif computador == 'tesoura' and jogada == 0:
    print('Jogador venceu!')
elif computador == 'tesoura' and jogada == 1:
    print('Computador venceu!')
else:
    print('EMPATE')

'''importando o módulo "sys", eu consegui usar o "sys.exit()". Com esse comando, eu consigo fazer o vcode
parar de ler o código na linha em que eu coloquei o comando "sys.exit()".'''

'''eu poderia ter feito a parte de escolha de opção (pedra, papel e tesoura) do computador de outra forma:
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
.
.
.
print('Computador jogou {}' .format(itens[computador]))


dessa forma, o módulo "randint" iria escolher aleatoriamente um numero de 0 a 2, porém, como no momento do
print eu estou declarando "itens[computador]" significa que a operação do "randint" atrelada à variável "computador"
irá ser executada dentro do nicho da variável "itens", sendo 0=pedra;1=papel e 2=tesoura. Portanto, o número que for
escolhido aleatoriamente pelo computador (devido à operação do "randint") será referente à posição de alguma 
das opções dentro da variável "itens".'''