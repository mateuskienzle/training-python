n = [[], []]
valor = 0
for c in range (1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor%2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
print('=-' *30)
n[0].sort()
n[1].sort()
print(f'Os valores pares digitados foram: {n[0]}')
print(f'Os valores ímpares digitados foram: {n[1]}')