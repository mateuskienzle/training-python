n = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')))
print(f'Você digitou os valores: {n}')
if 9 in n:
    print(f'O valor 9 apareceu {n.count(9)} vezes')
else:
    print('O valor 9 não foi digitado')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado.')
print(f'Os valores pares digitados foram:', end=' ')
for c in n:
    if c%2 == 0:
        pares = c
        print(pares, end=' ')