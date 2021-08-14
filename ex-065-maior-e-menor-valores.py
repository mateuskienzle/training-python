c = 0
soma = 0
maior = 0
menor = 0
pergunta = ''
while pergunta != 'N':
    num = int(input('Digite um número: '))
    pergunta = str(input('Deseja continuar? [S/N] ')).upper()
    soma += num
    c += 1
    if c == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
if pergunta == 'N':
    media = (soma/c)
    print('Você digitou {} números e a média entre eles é {}. ' .format(c, media))
    print('O maior valor foi {} e o menor foi {}.' .format(maior, menor))