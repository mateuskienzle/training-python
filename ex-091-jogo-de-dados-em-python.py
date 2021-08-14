from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = list()
print('=-' *15)
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key= itemgetter(1), reverse=True)
print('=-' *15)
print('= RANKING DOS JOGADORES =')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar foi {v[0]} com o valor {v[1]}.')
    sleep(1)