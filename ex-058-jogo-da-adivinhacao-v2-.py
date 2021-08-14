from random import randint
print ('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.')
print('Você consegue adivinhar?')
computador = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente de novo.')
        elif jogador > computador:
            print('Menos... Tente de novo.')
print('Acertou com {} tentativas. Boa!' .format(palpite))