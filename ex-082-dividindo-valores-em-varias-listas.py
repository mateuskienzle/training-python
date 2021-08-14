valores = list()
pares = list()
impares = list()
while True:
    n = (int(input('Digite um valor: ')))
    valores.append(n)
    if n% 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    pergunta = str(input('Quer continuar [S/N]? ')).upper()[0]
    if pergunta == 'N':
        break
print('=-' *30)
print(f'A lista completa é {valores}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')