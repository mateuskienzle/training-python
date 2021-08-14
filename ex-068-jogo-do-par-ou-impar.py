from random import randint
c = 0
print('=-' *15 )
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' *15 )
while True:
    n = int(input('Diga um valor: '))
    while True:
        jogador = str(input('Par ou Ímpar [P/I]?: ')).upper()[0]
        if jogador == 'P':
            jogador = 'PAR'
            break
        elif jogador == 'I':
            jogador = 'IMPAR'
            break
    print('-' *30 )
    computador = randint(1, 99)
    soma = (n+computador)
    if (soma%2) == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print(f'Você jogou {n} e o computador {computador}. Total de {soma} -> deu {resultado}')
    print('-' *30 )
    if resultado == jogador:
        c += 1
        print('Você venceu!')
        print('Vamos jogar novamente...')
        print('=-' *15)
    else:
        print('Você perdeu!')
        print('=-' *15)
        if c == 1:
            print(f'GAME OVER! Você venceu {c} vez.')
        else:
            print(f'GAME OVER! Você venceu {c} vezes.')
        break

''' NESSE EU FUI BRABÍSSIMO!!!'''