valores = []
for c in range (0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
valor_max = max(valores)
valor_min = min(valores)
print('=-' *30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {valor_max} nas posições ', end='')
for i, v in enumerate(valores):
    if v == valor_max:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {valor_min} nas posições ', end='')
for i, v in enumerate(valores):
    if v == valor_min:
        print(f'{i}...', end='')